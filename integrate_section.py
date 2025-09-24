#!/usr/bin/env python3
"""
Script to integrate the comprehensive Dog Health section into the full site
"""

import os
import re

def integrate_dog_health_section():
    # File paths
    full_site_path = r"D:\IDLS\Dog Leashes\IDLS site to be improved\improve it\Dog Health\IDLS_site_updated.html"
    comprehensive_path = r"D:\IDLS\Dog Leashes\IDLS site to be improved\improve it\Dog Health\comprehensive_dog_health_section_base64.html"
    output_path = r"D:\IDLS\rewrite.html"

    print(f"Reading full site from: {full_site_path}")
    print(f"Reading comprehensive section from: {comprehensive_path}")
    print(f"Output will be saved to: {output_path}")

    # Read the comprehensive Dog Health section
    with open(comprehensive_path, 'r', encoding='utf-8') as f:
        comprehensive_content = f.read()

    # Extract just the Dog Health div content
    dog_health_match = re.search(r'(<div id="dog-health"[^>]*>.*?</div>)', comprehensive_content, re.DOTALL)
    if not dog_health_match:
        print("Error: Could not find Dog Health section in comprehensive file")
        return

    new_dog_health_section = dog_health_match.group(1)
    print(f"Found new Dog Health section: {len(new_dog_health_section)} characters")

    # Read the full site in chunks to handle large file
    with open(full_site_path, 'r', encoding='utf-8') as f:
        full_site_content = f.read()

    # Find and replace the existing Dog Health section
    pattern = r'(<div id="dog-health"[^>]*>.*?</div>)'
    replacement = new_dog_health_section

    # Perform the replacement
    updated_content = re.sub(pattern, replacement, full_site_content, flags=re.DOTALL)

    # Check if replacement was successful
    if updated_content == full_site_content:
        print("Warning: No replacement made. Dog Health section may not exist in full site.")
        # Let's try to find where to insert it
        nav_match = re.search(r'(<a[^>]*href="#"[^>]*data-section="dog-health"[^>]*>.*?</a>)', updated_content, re.DOTALL)
        if nav_match:
            print("Found navigation link for Dog Health. Will attempt to insert after navigation.")
    else:
        print(f"Successfully replaced Dog Health section")

    # Write the updated content to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Successfully saved integrated site to: {output_path}")

    # Verify the file was created
    if os.path.exists(output_path):
        file_size = os.path.getsize(output_path)
        print(f"Output file size: {file_size:,} bytes ({file_size / 1024 / 1024:.1f} MB)")

        # Count base64 images in the output
        base64_count = updated_content.count('data:image/jpeg;base64,')
        print(f"Number of base64 images in output: {base64_count}")
    else:
        print("Error: Output file was not created")

if __name__ == "__main__":
    integrate_dog_health_section()