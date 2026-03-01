# Create the combine_names function here
def combine_names (name, surname):
    return name + ' ' + surname

if __name__ == '__main__':
    assert combine_names('James', 'Stevens') == 'James Stevens'
    assert combine_names('John', 'Resig') == 'John Resig'
    assert combine_names('Karl', 'Popper') == 'Karl Popper'