#!/usr/bin/env python3
import sys

try:
    import pypdf
    
    def extract_pdf(pdf_path, output_path):
        with open(pdf_path, 'rb') as pdf_file:
            reader = pypdf.PdfReader(pdf_file)
            text = ''
            for i, page in enumerate(reader.pages):
                text += f'\n--- Page {i+1} ---\n'
                text += page.extract_text()
            
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
            
            print(f"Extracted {len(reader.pages)} pages to {output_path}")
    
    if __name__ == '__main__':
        extract_pdf(sys.argv[1], sys.argv[2])
        
except ImportError:
    print("pypdf not installed. Trying PyPDF2...")
    try:
        import PyPDF2
        
        def extract_pdf(pdf_path, output_path):
            with open(pdf_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                text = ''
                for i, page in enumerate(reader.pages):
                    text += f'\n--- Page {i+1} ---\n'
                    text += page.extract_text()
                
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(text)
                
                print(f"Extracted {len(reader.pages)} pages to {output_path}")
        
        if __name__ == '__main__':
            extract_pdf(sys.argv[1], sys.argv[2])
    except ImportError:
        print("Neither pypdf nor PyPDF2 is installed. Please install one: pip install pypdf")
        sys.exit(1)
