from functools import wraps 

def add_wrapping(item):
    @wraps(item)
    def wrapped_item():
        return f"Wrapped up box of {str(item())}"
    return wrapped_item
def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return f"{style} Wrapped up box of {str(item())}"
        return wrapped_item
    return add_wrapping


@add_wrapping_with_style("Beautifully")
def new_gpu():
    return "A Brand New NVIDIA DGX A100 GPU"

print(new_gpu())
print(new_gpu.__name__)

