"""
Develop an Object-Oriented (OO) Python project that reads either a string or a list,
 then performs two analyses:
Calculates the total length.
Determines the number of uppercase characters.
The project should be structured with appropriate classes and methods. 
After implementation, use Pylint to analyzeand improve the code quality, 
ensuring adherence to Python’s best practices and style guidelines. 
 Share the result when you have done
"""

class TextAnalyzer:
    """A class to analyze text for length and uppercase character count."""
    def calculate_length(self, text)-> int:
        """Calculate the length of the input text."""

        if isinstance(text, str):
            return len(text)
        elif isinstance(text, list):
            return sum(len(item) for item in text if isinstance(item, str))
        return -1

    def count_uppercase(self, text) -> int:
        """Count the number of uppercase characters in the input text."""
        if isinstance(text, str):
            return sum(1 for char in text if char.isupper())
        elif isinstance(text, list):
            return sum(self.count_uppercase(item) for item in text if isinstance(item, str))
        else:
            return -1
    
    def count_digits(self,text) -> int:
       """Count the number of digit characters in the input text."""
       if isinstance(text,str):
           return sum(1 for item in text if item.isdigit())
       elif isinstance(text,list):
           return sum(self.count_digits(item) for item in text if isinstance(item,str))
       else:
           return -1
       
    def count_special_characters(self,text) -> int:
       """Count the number of special characters in the input text."""
       if isinstance(text,str):
           return sum(1 for item in text if (not item.isalnum()) and not item.isspace())
       elif isinstance(text,list):
           return sum(self.count_special_characters(item) for item in text if isinstance(item,str))
       else:
            return -1
       



def main():
    """Main function to test the text analysis."""
    text_prepare = input("Please enter a String :")
    analyzer = TextAnalyzer()
    length = analyzer.calculate_length(text_prepare)
    print(f"Length of the input: {length}")
    uppercase_count = analyzer.count_uppercase(text_prepare)
    print(f"Number of uppercase characters: {uppercase_count}")

    special_char_count = analyzer.count_special_characters(text_prepare)
    print(f"Number of special characters: {special_char_count}")
    digit_count = analyzer.count_digits(text_prepare)
    print(f"Number of digit characters: {digit_count}")

if __name__ == "__main__":
    main()
