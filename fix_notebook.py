import json
import nbformat
from nbformat import v4 as nbf

def validate_and_repair_notebook(notebook_path):
    try:
        # Load the notebook 
        with open(notebook_path, 'r') as f:
            notebook = nbformat.read(f, as_version=4)

        # Validate the notebook 
        errors = nbformat.validate(notebook)
        if errors:
            print(f"Notebook {notebook_path} has validation errors:")
            for error in errors:
                print(error)
            
        # Repair the notebook: just example adjustments, depending on errors found
        # In real scenarios, you might want to specifically fix certain errors
        if notebook['cells']:
            for cell in notebook['cells']:
                if cell['cell_type'] == 'code' and not cell['source'].strip():
                    # Example fix: remove empty code cells
                    notebook['cells'].remove(cell)

        # Save the repaired notebook
        with open(notebook_path, 'w') as f:
            nbformat.write(notebook, f)
        print(f"Notebook {notebook_path} repaired and saved.")

    except Exception as e:
        print(f"An error occurred while processing {notebook_path}: {str(e)}")

# Example usage: 
# validate_and_repair_notebook('your_notebook.ipynb')
