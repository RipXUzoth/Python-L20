start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range:"))
squares = [i**2 for i in range(start, end + 1)]
even_squares = [num for num in squares if num % 2 == 0]
odd_squares = [num for num in squares if num % 2 != 0]
print(f"\nAll square values: {squares}")
print(f"Even square values: {even_squares}")
print(f"Odd square values: {odd_squares}")