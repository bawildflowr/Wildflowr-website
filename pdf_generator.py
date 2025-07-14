#!/usr/bin/env python3
# PDF Generation for Tarot Readings

import os
import sys
from datetime import datetime
from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader

class TarotPDFGenerator:
    def __init__(self, output_dir="/home/ubuntu/wildflowers_tarot_website/src/pdf_output"):
        """Initialize the PDF generator with output directory."""
        self.output_dir = output_dir
        self.template_dir = "/home/ubuntu/wildflowers_tarot_website/src/pdf_templates"
        
        # Create directories if they don't exist
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.template_dir, exist_ok=True)
        
        # Set up Jinja2 environment
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
    
    def create_tarot_reading_pdf(self, order_data):
        """
        Generate a PDF for a tarot reading.
        
        Args:
            order_data (dict): Dictionary containing order information:
                - order_id: Unique order identifier
                - customer_name: Name of the customer
                - customer_email: Email of the customer
                - spread_type: Type of tarot spread
                - cards: List of cards with their positions and meanings
                - question: Customer's question (optional)
                - reading_date: Date of the reading
        
        Returns:
            str: Path to the generated PDF file
        """
        # Load the template
        template = self.env.get_template('tarot_reading_template.html')
        
        # Render the template with order data
        html_content = template.render(
            order_id=order_data.get('order_id'),
            customer_name=order_data.get('customer_name'),
            spread_type=order_data.get('spread_type'),
            cards=order_data.get('cards', []),
            question=order_data.get('question', ''),
            reading_date=order_data.get('reading_date', datetime.now().strftime('%B %d, %Y')),
            generation_date=datetime.now().strftime('%B %d, %Y')
        )
        
        # Generate PDF filename
        filename = f"tarot_reading_{order_data.get('order_id')}.pdf"
        output_path = os.path.join(self.output_dir, filename)
        
        # Generate PDF
        HTML(string=html_content).write_pdf(
            output_path,
            stylesheets=[
                CSS(string='''
                    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Poppins:wght@300;400;500;600&display=swap');
                    
                    body {
                        font-family: 'Poppins', sans-serif;
                        line-height: 1.6;
                        color: #333333;
                        margin: 0;
                        padding: 0;
                    }
                    
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    
                    .header {
                        text-align: center;
                        margin-bottom: 30px;
                        border-bottom: 2px solid #6b4e71;
                        padding-bottom: 20px;
                    }
                    
                    .logo {
                        font-family: 'Playfair Display', serif;
                        font-size: 28px;
                        color: #6b4e71;
                        margin: 0;
                    }
                    
                    .tagline {
                        font-style: italic;
                        color: #a67c52;
                    }
                    
                    h1, h2, h3, h4 {
                        font-family: 'Playfair Display', serif;
                        color: #2e2639;
                    }
                    
                    .reading-info {
                        background-color: #f5f0f6;
                        padding: 15px;
                        border-radius: 8px;
                        margin-bottom: 20px;
                    }
                    
                    .reading-info p {
                        margin: 5px 0;
                    }
                    
                    .question {
                        font-style: italic;
                        border-left: 3px solid #a67c52;
                        padding-left: 15px;
                        margin: 20px 0;
                    }
                    
                    .cards-section {
                        margin: 30px 0;
                    }
                    
                    .card {
                        margin-bottom: 30px;
                        padding-bottom: 20px;
                        border-bottom: 1px solid #eee;
                    }
                    
                    .card-header {
                        display: flex;
                        align-items: center;
                        margin-bottom: 15px;
                    }
                    
                    .card-image {
                        width: 100px;
                        margin-right: 20px;
                    }
                    
                    .card-title {
                        margin: 0;
                    }
                    
                    .card-position {
                        color: #6b4e71;
                        font-weight: 500;
                    }
                    
                    .card-meaning {
                        margin-top: 10px;
                    }
                    
                    .footer {
                        margin-top: 40px;
                        text-align: center;
                        font-size: 12px;
                        color: #666;
                    }
                    
                    .disclaimer {
                        font-size: 11px;
                        border-top: 1px solid #eee;
                        padding-top: 20px;
                        margin-top: 40px;
                    }
                    
                    @page {
                        margin: 1cm;
                    }
                ''')
            ]
        )
        
        return output_path
    
    def create_palm_reading_pdf(self, order_data):
        """
        Generate a PDF for a palm reading.
        
        Args:
            order_data (dict): Dictionary containing order information:
                - order_id: Unique order identifier
                - customer_name: Name of the customer
                - customer_email: Email of the customer
                - dominant_hand: Customer's dominant hand
                - palm_images: List of paths to palm images
                - birth_date: Customer's birth date (optional)
                - focus_areas: Areas to focus on in the reading (optional)
                - reading_date: Date of the reading
                - analysis: Dictionary containing analysis sections
        
        Returns:
            str: Path to the generated PDF file
        """
        # Load the template
        template = self.env.get_template('palm_reading_template.html')
        
        # Render the template with order data
        html_content = template.render(
            order_id=order_data.get('order_id'),
            customer_name=order_data.get('customer_name'),
            dominant_hand=order_data.get('dominant_hand'),
            palm_images=order_data.get('palm_images', []),
            birth_date=order_data.get('birth_date', ''),
            focus_areas=order_data.get('focus_areas', ''),
            reading_date=order_data.get('reading_date', datetime.now().strftime('%B %d, %Y')),
            analysis=order_data.get('analysis', {}),
            generation_date=datetime.now().strftime('%B %d, %Y')
        )
        
        # Generate PDF filename
        filename = f"palm_reading_{order_data.get('order_id')}.pdf"
        output_path = os.path.join(self.output_dir, filename)
        
        # Generate PDF
        HTML(string=html_content).write_pdf(
            output_path,
            stylesheets=[
                CSS(string='''
                    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Poppins:wght@300;400;500;600&display=swap');
                    
                    body {
                        font-family: 'Poppins', sans-serif;
                        line-height: 1.6;
                        color: #333333;
                        margin: 0;
                        padding: 0;
                    }
                    
                    .container {
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    
                    .header {
                        text-align: center;
                        margin-bottom: 30px;
                        border-bottom: 2px solid #6b4e71;
                        padding-bottom: 20px;
                    }
                    
                    .logo {
                        font-family: 'Playfair Display', serif;
                        font-size: 28px;
                        color: #6b4e71;
                        margin: 0;
                    }
                    
                    .tagline {
                        font-style: italic;
                        color: #a67c52;
                    }
                    
                    h1, h2, h3, h4 {
                        font-family: 'Playfair Display', serif;
                        color: #2e2639;
                    }
                    
                    .reading-info {
                        background-color: #f5f0f6;
                        padding: 15px;
                        border-radius: 8px;
                        margin-bottom: 20px;
                    }
                    
                    .reading-info p {
                        margin: 5px 0;
                    }
                    
                    .palm-images {
                        display: flex;
                        justify-content: space-between;
                        margin: 30px 0;
                        flex-wrap: wrap;
                    }
                    
                    .palm-image-container {
                        width: 48%;
                        margin-bottom: 20px;
                    }
                    
                    .palm-image {
                        width: 100%;
                        border: 1px solid #ddd;
                        border-radius: 8px;
                    }
                    
                    .palm-image-caption {
                        text-align: center;
                        margin-top: 10px;
                        font-style: italic;
                    }
                    
                    .analysis-section {
                        margin: 30px 0;
                        padding-bottom: 20px;
                        border-bottom: 1px solid #eee;
                    }
                    
                    .analysis-title {
                        color: #6b4e71;
                        border-bottom: 1px solid #a67c52;
                        padding-bottom: 5px;
                    }
                    
                    .footer {
                        margin-top: 40px;
                        text-align: center;
                        font-size: 12px;
                        color: #666;
                    }
                    
                    .disclaimer {
                        font-size: 11px;
                        border-top: 1px solid #eee;
                        padding-top: 20px;
                        margin-top: 40px;
                    }
                    
                    @page {
                        margin: 1cm;
                    }
                ''')
            ]
        )
        
        return output_path

# Example usage
if __name__ == "__main__":
    # Create generator
    generator = TarotPDFGenerator()
    
    # Example tarot reading data
    tarot_data = {
        'order_id': 'WFT12345',
        'customer_name': 'Jane Smith',
        'customer_email': 'jane@example.com',
        'spread_type': 'Celtic Cross',
        'question': 'What career path should I pursue in the coming year?',
        'reading_date': 'May 23, 2025',
        'cards': [
            {
                'name': 'The Fool',
                'position': 'Present',
                'image': '../images/cards/fool.jpg',
                'meaning': 'You are at the beginning of a new journey or phase in your career. This card suggests taking a leap of faith and embracing new opportunities without fear.'
            },
            {
                'name': 'The Magician',
                'position': 'Challenge',
                'image': '../images/cards/magician.jpg',
                'meaning': 'You have all the tools and resources you need to succeed. The challenge is to recognize your own power and use your skills effectively.'
            },
            # Additional cards would be included here
        ]
    }
    
    # Example palm reading data
    palm_data = {
        'order_id': 'WFT67890',
        'customer_name': 'John Doe',
        'customer_email': 'john@example.com',
        'dominant_hand': 'Right',
        'birth_date': 'April 15, 1985',
        'focus_areas': 'Career and relationships',
        'reading_date': 'May 23, 2025',
        'palm_images': [
            {'path': '../images/palm-samples/right-palm.jpg', 'caption': 'Right Hand (Dominant)'},
            {'path': '../images/palm-samples/left-palm.jpg', 'caption': 'Left Hand (Non-Dominant)'}
        ],
        'analysis': {
            'life_line': 'Your life line indicates a strong vitality and enthusiasm for life. The depth and clarity of the line suggest good health and resilience.',
            'heart_line': 'Your heart line reveals a passionate and emotional nature. The branches toward your fingers indicate strong romantic relationships.',
            'head_line': 'The head line shows analytical thinking and creative problem-solving abilities. Its connection to your life line suggests a cautious approach to new ventures.',
            'fate_line': 'Your fate line indicates a strong sense of purpose and career focus. The clarity in the middle section suggests a successful period in your 30s and 40s.',
            'mounts': 'The prominent Mount of Jupiter indicates leadership qualities and ambition. The Mount of Venus shows a capacity for deep emotional connections and creativity.',
            'overall': 'Overall, your palms reveal a balanced individual with strong potential for both career success and meaningful relationships. The coming year appears particularly favorable for professional advancement.'
        }
    }
    
    # Generate PDFs
    tarot_pdf_path = generator.create_tarot_reading_pdf(tarot_data)
    palm_pdf_path = generator.create_palm_reading_pdf(palm_data)
    
    print(f"Tarot reading PDF generated: {tarot_pdf_path}")
    print(f"Palm reading PDF generated: {palm_pdf_path}")
