// Tarot Reading System JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const spreadButtons = document.querySelectorAll('.select-spread-btn');
    const cardSelectionSection = document.getElementById('card-selection-section');
    const orderFormSection = document.getElementById('order-form-section');
    const orderConfirmationSection = document.getElementById('order-confirmation-section');
    const tarotDeck = document.getElementById('tarot-deck');
    const selectedCardsDisplay = document.getElementById('selected-cards-display');
    const resetSelectionBtn = document.getElementById('reset-selection-btn');
    const continueToCheckoutBtn = document.getElementById('continue-to-checkout-btn');
    const backToSelectionBtn = document.getElementById('back-to-selection-btn');
    const completeOrderBtn = document.getElementById('complete-order-btn');
    const createAccountCheckbox = document.getElementById('create-account');
    const accountFields = document.getElementById('account-fields');
    const readingOrderForm = document.getElementById('reading-order-form');
    
    // Spread selection variables
    let selectedSpread = '';
    let selectedSpreadName = '';
    let cardsToSelect = 0;
    let selectedCards = [];
    let spreadPrice = 0;
    
    // Tarot deck data - major arcana only for demo
    const tarotCards = [
        { id: 1, name: 'The Fool', image: 'images/cards/fool.jpg' },
        { id: 2, name: 'The Magician', image: 'images/cards/magician.jpg' },
        { id: 3, name: 'The High Priestess', image: 'images/cards/high-priestess.jpg' },
        { id: 4, name: 'The Empress', image: 'images/cards/empress.jpg' },
        { id: 5, name: 'The Emperor', image: 'images/cards/emperor.jpg' },
        { id: 6, name: 'The Hierophant', image: 'images/cards/hierophant.jpg' },
        { id: 7, name: 'The Lovers', image: 'images/cards/lovers.jpg' },
        { id: 8, name: 'The Chariot', image: 'images/cards/chariot.jpg' },
        { id: 9, name: 'Strength', image: 'images/cards/strength.jpg' },
        { id: 10, name: 'The Hermit', image: 'images/cards/hermit.jpg' },
        { id: 11, name: 'Wheel of Fortune', image: 'images/cards/wheel-of-fortune.jpg' },
        { id: 12, name: 'Justice', image: 'images/cards/justice.jpg' },
        { id: 13, name: 'The Hanged Man', image: 'images/cards/hanged-man.jpg' },
        { id: 14, name: 'Death', image: 'images/cards/death.jpg' },
        { id: 15, name: 'Temperance', image: 'images/cards/temperance.jpg' },
        { id: 16, name: 'The Devil', image: 'images/cards/devil.jpg' },
        { id: 17, name: 'The Tower', image: 'images/cards/tower.jpg' },
        { id: 18, name: 'The Star', image: 'images/cards/star.jpg' },
        { id: 19, name: 'The Moon', image: 'images/cards/moon.jpg' },
        { id: 20, name: 'The Sun', image: 'images/cards/sun.jpg' },
        { id: 21, name: 'Judgement', image: 'images/cards/judgement.jpg' },
        { id: 22, name: 'The World', image: 'images/cards/world.jpg' }
    ];
    
    // Initialize the tarot deck display
    function initializeTarotDeck() {
        // Clear the deck
        tarotDeck.innerHTML = '';
        
        // Shuffle the cards
        const shuffledDeck = [...tarotCards].sort(() => Math.random() - 0.5);
        
        // Create card elements
        shuffledDeck.forEach(card => {
            const cardElement = document.createElement('div');
            cardElement.className = 'tarot-card';
            cardElement.dataset.cardId = card.id;
            cardElement.dataset.cardName = card.name;
            cardElement.dataset.cardImage = card.image;
            
            // Card back (shown initially)
            const cardBack = document.createElement('div');
            cardBack.className = 'card-back';
            cardBack.innerHTML = '<img src="images/card-back.jpg" alt="Card Back">';
            
            cardElement.appendChild(cardBack);
            tarotDeck.appendChild(cardElement);
            
            // Add click event
            cardElement.addEventListener('click', handleCardSelection);
        });
    }
    
    // Handle spread selection
    spreadButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Get spread data
            selectedSpread = this.dataset.spread;
            spreadPrice = parseInt(this.dataset.price);
            
            // Set cards to select based on spread
            switch(selectedSpread) {
                case 'single':
                    cardsToSelect = 1;
                    selectedSpreadName = 'Single Card Reading';
                    break;
                case 'two-card':
                    cardsToSelect = 2;
                    selectedSpreadName = 'Two Card Reading';
                    break;
                case 'three-card':
                    cardsToSelect = 3;
                    selectedSpreadName = 'Three Card Reading';
                    break;
                case 'five-card':
                    cardsToSelect = 5;
                    selectedSpreadName = 'Five Card Reading';
                    break;
                case 'celtic-cross':
                    cardsToSelect = 10;
                    selectedSpreadName = 'Celtic Cross Reading';
                    break;
            }
            
            // Update UI
            document.getElementById('selected-spread-name').textContent = selectedSpreadName;
            document.getElementById('cards-to-select').textContent = cardsToSelect;
            document.getElementById('cards-selected').textContent = '0';
            
            // Reset selected cards
            selectedCards = [];
            selectedCardsDisplay.innerHTML = '';
            
            // Initialize the deck
            initializeTarotDeck();
            
            // Show card selection section
            cardSelectionSection.style.display = 'block';
            
            // Scroll to card selection section
            cardSelectionSection.scrollIntoView({ behavior: 'smooth' });
            
            // Disable continue button until all cards are selected
            continueToCheckoutBtn.disabled = true;
        });
    });
    
    // Handle card selection
    function handleCardSelection() {
        // Check if card is already selected
        if (this.classList.contains('selected')) {
            return;
        }
        
        // Check if we've reached the maximum number of cards
        if (selectedCards.length >= cardsToSelect) {
            alert(`You can only select ${cardsToSelect} cards for this spread. Please reset your selection to choose different cards.`);
            return;
        }
        
        // Mark card as selected
        this.classList.add('selected');
        
        // Get card data
        const cardId = this.dataset.cardId;
        const cardName = this.dataset.cardName;
        const cardImage = this.dataset.cardImage;
        
        // Add to selected cards array
        selectedCards.push({
            id: cardId,
            name: cardName,
            image: cardImage
        });
        
        // Update selected cards display
        updateSelectedCardsDisplay();
        
        // Update count
        document.getElementById('cards-selected').textContent = selectedCards.length;
        
        // Enable continue button if all cards are selected
        if (selectedCards.length === cardsToSelect) {
            continueToCheckoutBtn.disabled = false;
        }
    }
    
    // Update the selected cards display
    function updateSelectedCardsDisplay() {
        selectedCardsDisplay.innerHTML = '';
        
        selectedCards.forEach((card, index) => {
            const cardElement = document.createElement('div');
            cardElement.className = 'selected-card';
            
            const cardImage = document.createElement('img');
            cardImage.src = card.image;
            cardImage.alt = card.name;
            
            const cardName = document.createElement('p');
            cardName.textContent = card.name;
            
            const cardPosition = document.createElement('span');
            cardPosition.className = 'card-position';
            cardPosition.textContent = `Card ${index + 1}`;
            
            cardElement.appendChild(cardImage);
            cardElement.appendChild(cardName);
            cardElement.appendChild(cardPosition);
            
            selectedCardsDisplay.appendChild(cardElement);
        });
    }
    
    // Reset card selection
    resetSelectionBtn.addEventListener('click', function() {
        // Clear selected cards
        selectedCards = [];
        selectedCardsDisplay.innerHTML = '';
        
        // Reset card elements
        const cardElements = document.querySelectorAll('.tarot-card');
        cardElements.forEach(card => {
            card.classList.remove('selected');
        });
        
        // Update count
        document.getElementById('cards-selected').textContent = '0';
        
        // Disable continue button
        continueToCheckoutBtn.disabled = true;
    });
    
    // Continue to checkout
    continueToCheckoutBtn.addEventListener('click', function() {
        // Update order summary
        document.getElementById('summary-spread-type').textContent = selectedSpreadName;
        document.getElementById('summary-card-count').textContent = cardsToSelect;
        document.getElementById('summary-price').textContent = spreadPrice;
        
        // Hide card selection, show order form
        cardSelectionSection.style.display = 'none';
        orderFormSection.style.display = 'block';
        
        // Scroll to order form
        orderFormSection.scrollIntoView({ behavior: 'smooth' });
    });
    
    // Back to card selection
    backToSelectionBtn.addEventListener('click', function() {
        // Hide order form, show card selection
        orderFormSection.style.display = 'none';
        cardSelectionSection.style.display = 'block';
        
        // Scroll to card selection
        cardSelectionSection.scrollIntoView({ behavior: 'smooth' });
    });
    
    // Toggle account fields
    createAccountCheckbox.addEventListener('change', function() {
        accountFields.style.display = this.checked ? 'block' : 'none';
    });
    
    // Handle order submission
    readingOrderForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // In a real implementation, we would:
        // 1. Validate the form
        // 2. Process the payment
        // 3. Save the order to the database
        // 4. Generate a unique order number
        // 5. Send confirmation email
        
        // For demo purposes, we'll just show the confirmation
        const orderNumber = 'WFT' + Math.floor(10000 + Math.random() * 90000);
        const userEmail = document.getElementById('email').value;
        
        document.getElementById('confirmation-order-number').textContent = orderNumber;
        document.getElementById('confirmation-email').textContent = userEmail;
        
        // Hide order form, show confirmation
        orderFormSection.style.display = 'none';
        orderConfirmationSection.style.display = 'block';
        
        // Scroll to confirmation
        orderConfirmationSection.scrollIntoView({ behavior: 'smooth' });
        
        // Show/hide account button based on account creation
        document.getElementById('view-account-btn').style.display = 
            createAccountCheckbox.checked ? 'inline-block' : 'none';
    });
});
