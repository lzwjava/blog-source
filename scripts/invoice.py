import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

INVOICE_DIR = "invoice"

def generate_invoice(bill_to, details, total_cny, output_path="invoice.pdf"):
    """
    Generates an invoice PDF using LaTeX.

    Args:
        bill_to (str): The billing address.
        details (str): A description of the items being billed.
        total_cny (float): The total amount in CNY.
        output_path (str): The desired output path for the PDF.
    """

    # Create the invoice directory if it doesn't exist
    if not os.path.exists(INVOICE_DIR):
        os.makedirs(INVOICE_DIR)

    output_path = os.path.join(INVOICE_DIR, output_path)
    logging.info(f"Generating invoice to: {output_path}")

    # Read the LaTeX template from file
    try:
        with open("latex/en/invoice-en.tex", "r") as tex_file:
            latex_template = tex_file.read()
        logging.info("LaTeX template read successfully.")
    except FileNotFoundError:
        logging.error("LaTeX template file not found!")
        return

    # Replace placeholders in the LaTeX template
    latex_template = latex_template.replace("Your Address Here", "Your Address Here")
    latex_template = latex_template.replace("Your City, Postal Code", "Your City, Postal Code")
    latex_template = latex_template.replace("your_email@example.com", "your_email@example.com")
    latex_template = latex_template.replace(r"\section*{Bill to}\n\noindent", r"\section*{Bill to}\n\noindent" + bill_to)
    latex_template = latex_template.replace(r"\section*{Details}\n\noindent", r"\section*{Details}\n\noindent" + details)
    latex_template = latex_template.replace(r"\textbf{800.00}", r"\textbf{" + str(total_cny) + "}")

    # Save the LaTeX code to a temporary file in the invoice directory
    tex_file_path = os.path.join(INVOICE_DIR, "invoice.tex")
    with open(tex_file_path, "w") as tex_file:
        tex_file.write(latex_template)
    logging.info("LaTeX code written to invoice.tex")

    # Compile the LaTeX code to PDF using xelatex
    try:
        subprocess.run(["xelatex", tex_file_path], check=True, capture_output=True, cwd=INVOICE_DIR)
        # Rename the PDF to the desired output path
        pdf_file_path = os.path.join(INVOICE_DIR, "invoice.pdf")
        os.rename(pdf_file_path, output_path)
        logging.info(f"Invoice generated successfully at {output_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error generating invoice: {e.stderr.decode('utf-8')}")
    finally:
        # Clean up temporary files
        temp_files = [
            os.path.join(INVOICE_DIR, "invoice.tex"),
            os.path.join(INVOICE_DIR, "invoice.log"),
            os.path.join(INVOICE_DIR, "invoice.aux")
        ]
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except FileNotFoundError:
                logging.warning(f"Temporary file not found during cleanup: {temp_file}")
        logging.info("Temporary files cleaned up.")


if __name__ == '__main__':
    # Example usage
    bill_to_address = """
Client Name\\
Client Address\\
Client City, Postal Code
"""

    invoice_details = """
Item 1: Description of item 1 - 100 CNY\\
Item 2: Description of item 2 - 200 CNY\\
Service Fee: Consulting - 500 CNY
"""

    total_amount = 800.00

    generate_invoice(bill_to_address, invoice_details, total_amount, "my_invoice.pdf")
