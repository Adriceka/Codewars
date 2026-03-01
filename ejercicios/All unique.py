def has_unique_chars(string):
    return len(string) == len(set(string))

if __name__ == '__main__':
        assert has_unique_chars("abcdef") == True
        assert has_unique_chars("++-") == False
        assert has_unique_chars("  nAa") == False