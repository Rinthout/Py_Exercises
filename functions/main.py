# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# Part 1
def greet(a):
    return f"Hello, {a}!"

print(greet('Bob'))
          
# Part 2
def add(a, b, c):
    return a + b + c

print(add(5, 3, 2))

# Part 3
def positive(a):
    if a > 0:
        return True
    else: 
        return False

print(positive(50))
print(positive(-50))
print(positive(0))

# Part 4:
def negative(a):
    if a < 0:
        return True
    else:
        return False

print(negative(50))
print(negative(-50))
print(negative(0))