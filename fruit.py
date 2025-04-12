def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")

#write code to reverse list
  fruit_list.reverse()
  print(fruit_list)

  #write code to append orange
  fruit_list.append("orange")
  print(fruit_list)

  #write code to find apple and and insert "cherry" before "apple" in the list and print the list.
  index = fruit_list.index("apple")
  fruit_list.insert(index,"cherry")
  print(f"Cherry added before apple", fruit_list)

  #Add code to remove "banana" from fruit_list and print the list.
  fruit_list.remove("banana")
  print(f"Banana removed", fruit_list)

  #Pop the last element from the list
  fruit_list.pop()
  print(f"Last item popped", fruit_list)


if __name__ == "__main__":
  main()


