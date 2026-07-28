const fs = require('fs');
const path = require('path');

const filepath = "d:\\GrowwPark projects\\LuxeTime\\contact.html";
let content = fs.readFileSync(filepath, 'utf-8');

const replacements = {
    "How May We Assist You?": "Custom Arrangement Enquiry",
    "Whether you are searching for a specific grand complication, seeking bespoke jewellery design, or require post-purchase support, please provide the details of your request below.": "Whether you are looking for a unique wedding bouquet, a custom sympathy arrangement, or specific seasonal flowers, please provide the details of your request below.",
    "<option value=\"purchase\">Product Purchase</option>": "<option value=\"custom\">Custom Arrangement</option>",
    "<option value=\"sourcing\">Watch Sourcing</option>": "<option value=\"wedding\">Wedding Flowers</option>",
    "<option value=\"service\">Servicing & Repair</option>": "<option value=\"delivery\">Same-Day Delivery Inquiry</option>",
    "<option value=\"press\">Press & Media</option>": "<option value=\"seasonal\">Seasonal Availability</option>",
    "Please provide specific details such as brand, reference number, or nature of your request...": "Please provide specific details such as preferred flowers, colors, sizes, or delivery date...",
    "Excellence is not a single act, but a habit. We look forward to serving you.": "Every petal tells a story. We look forward to crafting yours."
};

for (const [oldStr, newStr] of Object.entries(replacements)) {
    content = content.split(oldStr).join(newStr);
}

fs.writeFileSync(filepath, content, 'utf-8');
console.log("Updated contact.html");
