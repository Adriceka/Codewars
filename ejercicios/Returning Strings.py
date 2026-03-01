def greet(name):
  
    return "Hello, " + name + " how are you doing today?"

if __name__ == '__main__':
    assert greet('Ryan') == "Hello, Ryan how are you doing today?"
    assert greet('Nate') == "Hello, Nate how are you doing today?"
    assert greet('Raju') == "Hello, Raju how are you doing today?"