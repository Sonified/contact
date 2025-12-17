# Contact Page

This folder contains a standalone contact/links page for Robert Alexander's sonification work.

## Files

- `index.html` - Main contact page with embedded video, project links, and social media
- `Quantum_Background_Color.jpg` - Profile image (circular mask applied via CSS)
- `Breathscape_Logo_Square_1024x1024.jpg` - Breathscape project logo
- `contact_qr_code.png` - QR code linking to this page
- `generate_qr_code.py` - Python script to regenerate QR code

## URL

**Live page:** https://contact.now.audio

## Projects Listed

- Volcano Seismic Audification
- Space Weather Audification
- Breathscape
- HARP Citizen Science

## Social Links

- YouTube: @Sonification
- Instagram: @sonified
- Facebook: /Sonification
- LinkedIn: /in/sonification
- Email: robert@auralab.io

## Regenerating QR Code

```bash
python3 generate_qr_code.py
```

This will regenerate `contact_qr_code.png` pointing to https://contact.now.audio

## GitHub Pages Setup

1. Push this repo to GitHub
2. Go to repository Settings → Pages
3. Set Source to "Deploy from branch"
4. Set Branch to "main" and folder to "/ (root)"
5. The CNAME file will automatically configure the custom domain
6. Add DNS record: `CNAME contact CNAME username.github.io`
