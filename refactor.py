import os
import glob
import re

def main():
    directory = r"d:\GrowwPark projects\LuxeTime"
    html_files = glob.glob(os.path.join(directory, "*.html"))
    
    replacements = {
        "Watches.html": "Bouquets.html",
        "Jewellery.html": "Occasions.html",
        "Product.html": "Seasonal.html",
        "New Arrivals.html": "Delivery.html",
        "Gifting.html": "Gifts.html",
        
        ">Watches<": ">Bouquets<",
        ">Jewellery<": ">Occasions<",
        ">Product<": ">Seasonal<",
        ">Gifting<": ">Gifts<",
        ">New Arrivals<": ">Delivery Info<",
        
        "primary: '#050505'": "primary: '#EC4899'",
        "secondary: '#D4AF37'": "secondary: '#FFFFFF'",
        
        "hover:text-[#D4AF37]": "hover:text-[#EC4899]",
        "text-[#D4AF37]": "text-[#EC4899]",
        "bg-[#D4AF37]": "bg-[#EC4899]",
        "border-[#D4AF37]": "border-[#EC4899]",
        
        "LuxeTime": "BloomBoutique",
        "Luxe<span class=\"text-secondary\">Time</span>": "Bloom<span class=\"text-secondary\">Boutique</span>",
        "Timeless Luxury": "Fresh & Beautiful",
        "Luxury Watches": "Fresh Bouquets",
        "Gold Jewellery": "Wedding Flowers",
        "Diamond Collection": "Anniversary Bouquets",
        "Silver Collection": "Sympathy Flowers",
        "Rolex": "Roses",
        "Titan": "Lilies",
        "Casio": "Tulips",
        "Seiko": "Orchids",
        "Tissot": "Daisies",
        "Citizen": "Sunflowers",
        "The Perfect Present": "Say It With Flowers",
        "Exclusive Gift Collection": "Bouquets by Occasion",
        "Client Testimonials": "Happy Customers",
        "Elegance Validated": "Smiles Delivered",
        "Visit Our Showroom": "Visit Our Shop",
        
        "assets/images/premium/watch_hero_1.png": "https://images.unsplash.com/photo-1563241598-7299a9b70b57?w=1200&h=800&fit=crop",
        "assets/images/premium/showroom_hero.png": "https://images.unsplash.com/photo-1591886960571-74d43a9d4166?w=600&h=800&fit=crop",
        "assets/images/premium/jewellery_product_3.png": "https://images.unsplash.com/photo-1562690868-60bbe7293e94?w=600&h=800&fit=crop",
        "assets/images/img-4.jpg": "https://images.unsplash.com/photo-1582794543139-8ac9cb0f7b11?w=600&h=800&fit=crop",
        "assets/images/img-62.jpg": "https://images.unsplash.com/photo-1508610048659-a06b669e3321?w=600&h=800&fit=crop",
        "assets/images/img-6.jpg": "https://images.unsplash.com/photo-1523694576722-c361955fb8bf?w=1200&h=800&fit=crop",
        
        "fa-gem": "fa-seedling",
        "fa-ring": "fa-heart",
        "fa-glass-cheers": "fa-birthday-cake",
    }
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Specific CSS updates for hover effects
        content = re.sub(r'color:\s*#D4AF37', 'color: var(--text-heading)', content)
        content = re.sub(r'background-color:\s*rgba\(212,\s*175,\s*55,\s*0\.1\)', 'background-color: rgba(236, 72, 153, 0.1)', content)
        content = re.sub(r'rgba\(212,\s*175,\s*55,\s*0\.15\)', 'rgba(236, 72, 153, 0.15)', content)
        content = re.sub(r'border-color:\s*#D4AF37', 'border-color: #EC4899', content)
            
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"Refactored {len(html_files)} HTML files.")

if __name__ == '__main__':
    main()
