# Check keywords programmatically
import keyword

print(keyword.iskeyword("if"))  # True
print(keyword.iskeyword("hello"))  # False
print(keyword.kwlist)  # List of all Python keywords

