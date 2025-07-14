// Palm Reading System JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const startPalmReadingBtn = document.getElementById('start-palm-reading-btn');
    const ctaStartPalmReadingBtn = document.getElementById('cta-start-palm-reading-btn');
    const palmUploadSection = document.getElementById('palm-upload-section');
    const palmOrderFormSection = document.getElementById('palm-order-form-section');
    const palmConfirmationSection = document.getElementById('palm-confirmation-section');
    const dominantHandDropzone = document.getElementById('dominant-hand-dropzone');
    const nonDominantHandDropzone = document.getElementById('non-dominant-hand-dropzone');
    const dominantHandInput = document.getElementById('dominant-hand-input');
    const nonDominantHandInput = document.getElementById('non-dominant-hand-input');
    const dominantHandPreview = document.getElementById('dominant-hand-preview');
    const nonDominantHandPreview = document.getElementById('non-dominant-hand-preview');
    const dominantHandImg = document.getElementById('dominant-hand-img');
    const nonDominantHandImg = document.getElementById('non-dominant-hand-img');
    const removeImageBtns = document.querySelectorAll('.remove-image');
    const continueToCheckoutBtn = document.getElementById('continue-to-checkout-btn');
    const cancelUploadBtn = document.getElementById('cancel-upload-btn');
    const backToUploadBtn = document.getElementById('back-to-upload-btn');
    const palmCreateAccountCheckbox = document.getElementById('palm-create-account');
    const palmAccountFields = document.getElementById('palm-account-fields');
    const palmOrderForm = document.getElementById('palm-order-form');
    
    // Upload status
    let dominantHandUploaded = false;
    let nonDominantHandUploaded = false;
    
    // Show palm upload section
    function showPalmUploadSection() {
        palmUploadSection.style.display = 'block';
        palmUploadSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    // Event listeners for starting palm reading
    if (startPalmReadingBtn) {
        startPalmReadingBtn.addEventListener('click', showPalmUploadSection);
    }
    
    if (ctaStartPalmReadingBtn) {
        ctaStartPalmReadingBtn.addEventListener('click', showPalmUploadSection);
    }
    
    // Handle drag and drop for dominant hand
    if (dominantHandDropzone) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dominantHandDropzone.addEventListener(eventName, preventDefaults, false);
        });
        
        ['dragenter', 'dragover'].forEach(eventName => {
            dominantHandDropzone.addEventListener(eventName, () => {
                dominantHandDropzone.classList.add('highlight');
            }, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            dominantHandDropzone.addEventListener(eventName, () => {
                dominantHandDropzone.classList.remove('highlight');
            }, false);
        });
        
        dominantHandDropzone.addEventListener('drop', (e) => {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files.length) {
                handleDominantHandFile(files[0]);
            }
        }, false);
        
        dominantHandDropzone.addEventListener('click', () => {
            dominantHandInput.click();
        });
        
        dominantHandInput.addEventListener('change', () => {
            if (dominantHandInput.files.length) {
                handleDominantHandFile(dominantHandInput.files[0]);
            }
        });
    }
    
    // Handle drag and drop for non-dominant hand
    if (nonDominantHandDropzone) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            nonDominantHandDropzone.addEventListener(eventName, preventDefaults, false);
        });
        
        ['dragenter', 'dragover'].forEach(eventName => {
            nonDominantHandDropzone.addEventListener(eventName, () => {
                nonDominantHandDropzone.classList.add('highlight');
            }, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            nonDominantHandDropzone.addEventListener(eventName, () => {
                nonDominantHandDropzone.classList.remove('highlight');
            }, false);
        });
        
        nonDominantHandDropzone.addEventListener('drop', (e) => {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files.length) {
                handleNonDominantHandFile(files[0]);
            }
        }, false);
        
        nonDominantHandDropzone.addEventListener('click', () => {
            nonDominantHandInput.click();
        });
        
        nonDominantHandInput.addEventListener('change', () => {
            if (nonDominantHandInput.files.length) {
                handleNonDominantHandFile(nonDominantHandInput.files[0]);
            }
        });
    }
    
    // Prevent default drag behaviors
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    // Handle dominant hand file
    function handleDominantHandFile(file) {
        // Validate file type
        if (!file.type.match('image.*')) {
            alert('Please upload an image file (JPEG, PNG, etc.)');
            return;
        }
        
        // Display preview
        const reader = new FileReader();
        reader.onload = function(e) {
            dominantHandImg.src = e.target.result;
            dominantHandDropzone.style.display = 'none';
            dominantHandPreview.style.display = 'block';
            dominantHandUploaded = true;
            checkUploadStatus();
        };
        reader.readAsDataURL(file);
    }
    
    // Handle non-dominant hand file
    function handleNonDominantHandFile(file) {
        // Validate file type
        if (!file.type.match('image.*')) {
            alert('Please upload an image file (JPEG, PNG, etc.)');
            return;
        }
        
        // Display preview
        const reader = new FileReader();
        reader.onload = function(e) {
            nonDominantHandImg.src = e.target.result;
            nonDominantHandDropzone.style.display = 'none';
            nonDominantHandPreview.style.display = 'block';
            nonDominantHandUploaded = true;
            checkUploadStatus();
        };
        reader.readAsDataURL(file);
    }
    
    // Remove image
    removeImageBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const target = this.dataset.target;
            if (target === 'dominant') {
                dominantHandDropzone.style.display = 'block';
                dominantHandPreview.style.display = 'none';
                dominantHandInput.value = '';
                dominantHandUploaded = false;
            } else if (target === 'non-dominant') {
                nonDominantHandDropzone.style.display = 'block';
                nonDominantHandPreview.style.display = 'none';
                nonDominantHandInput.value = '';
                nonDominantHandUploaded = false;
            }
            checkUploadStatus();
        });
    });
    
    // Check if both hands are uploaded
    function checkUploadStatus() {
        if (dominantHandUploaded && nonDominantHandUploaded) {
            continueToCheckoutBtn.disabled = false;
        } else {
            continueToCheckoutBtn.disabled = true;
        }
    }
    
    // Continue to checkout
    if (continueToCheckoutBtn) {
        continueToCheckoutBtn.addEventListener('click', function() {
            // Validate form
            const dominantHandSelect = document.getElementById('dominant-hand');
            if (!dominantHandSelect.value) {
                alert('Please select which is your dominant hand.');
                return;
            }
            
            // Hide upload section, show order form
            palmUploadSection.style.display = 'none';
            palmOrderFormSection.style.display = 'block';
            
            // Scroll to order form
            palmOrderFormSection.scrollIntoView({ behavior: 'smooth' });
        });
    }
    
    // Cancel upload
    if (cancelUploadBtn) {
        cancelUploadBtn.addEventListener('click', function() {
            // Hide upload section
            palmUploadSection.style.display = 'none';
            
            // Reset upload status
            dominantHandDropzone.style.display = 'block';
            dominantHandPreview.style.display = 'none';
            nonDominantHandDropzone.style.display = 'block';
            nonDominantHandPreview.style.display = 'none';
            dominantHandInput.value = '';
            nonDominantHandInput.value = '';
            dominantHandUploaded = false;
            nonDominantHandUploaded = false;
            
            // Scroll back to service section
            document.querySelector('.palm-reading-service').scrollIntoView({ behavior: 'smooth' });
        });
    }
    
    // Back to upload
    if (backToUploadBtn) {
        backToUploadBtn.addEventListener('click', function() {
            // Hide order form, show upload section
            palmOrderFormSection.style.display = 'none';
            palmUploadSection.style.display = 'block';
            
            // Scroll to upload section
            palmUploadSection.scrollIntoView({ behavior: 'smooth' });
        });
    }
    
    // Toggle account fields
    if (palmCreateAccountCheckbox) {
        palmCreateAccountCheckbox.addEventListener('change', function() {
            palmAccountFields.style.display = this.checked ? 'block' : 'none';
        });
    }
    
    // Handle order submission
    if (palmOrderForm) {
        palmOrderForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // In a real implementation, we would:
            // 1. Validate the form
            // 2. Upload the palm images to secure storage
            // 3. Process the payment
            // 4. Save the order to the database
            // 5. Generate a unique order number
            // 6. Send confirmation email
            
            // For demo purposes, we'll just show the confirmation
            const orderNumber = 'WFT' + Math.floor(10000 + Math.random() * 90000);
            const userEmail = document.getElementById('palm-email').value;
            
            document.getElementById('palm-confirmation-order-number').textContent = orderNumber;
            document.getElementById('palm-confirmation-email').textContent = userEmail;
            
            // Hide order form, show confirmation
            palmOrderFormSection.style.display = 'none';
            palmConfirmationSection.style.display = 'block';
            
            // Scroll to confirmation
            palmConfirmationSection.scrollIntoView({ behavior: 'smooth' });
            
            // Show/hide account button based on account creation
            document.getElementById('palm-view-account-btn').style.display = 
                palmCreateAccountCheckbox.checked ? 'inline-block' : 'none';
        });
    }
});
