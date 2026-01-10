#!/usr/bin/env python3
import re

def convert_markdown_to_html(text):
    # Convert bold text
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<em><strong>\1</strong></em>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)

    # Convert links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" class="text-blue-600 hover:underline">\1</a>', text)

    # Convert bullet points
    lines = text.split('\n')
    in_list = False
    result_lines = []

    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                result_lines.append('<ul class="list-disc pl-6 space-y-2">')
                in_list = True
            result_lines.append(f'<li>{line.strip()[2:]}</li>')
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            result_lines.append(line)

    if in_list:
        result_lines.append('</ul>')

    text = '\n'.join(result_lines)

    # Convert headers (after # or numbered sections)
    text = re.sub(r'^# (.*?)$', r'<h1 class="text-3xl font-bold mb-4">\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^\*\*(\d+\. .*?)\*\*', r'<h2 id="section\1" class="text-2xl font-semibold mt-8 mb-4">\1</h2>', text, flags=re.MULTILINE)

    # Convert paragraphs
    text = re.sub(r'\n\n', '</p><p class="mb-4">', text)

    # Wrap tables
    text = re.sub(r'\| \*\*Category\*\* \|', '<div class="overflow-x-auto mb-4"><table class="min-w-full border"><thead><tr><th class="border px-4 py-2">Category</th>', text)

    return f'<div class="prose max-w-none"><p class="mb-4">{text}</p></div>'

# Read and convert privacy policy
with open('privacy-automail.txt', 'r') as f:
    privacy_content = f.read()

html_content = convert_markdown_to_html(privacy_content)

# Save converted content
with open('privacy-converted.html', 'w') as f:
    f.write(html_content)

print("Privacy policy converted to HTML")

# Read and convert terms
with open('tOs-automail.txt', 'r') as f:
    terms_content = f.read()

html_content = convert_markdown_to_html(terms_content)

# Save converted content
with open('terms-converted.html', 'w') as f:
    f.write(html_content)

print("Terms of service converted to HTML")
