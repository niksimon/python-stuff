nums = [4, 8, 11, 88, 15, 63, 77]
friends = ["Joe", "Jack", "Jessica", "Oscar", "Poe", "Tim", "Mike", "Jim"]

#friends.extend(nums)

friends.append("Bo")
friends.insert(3, "Kelly")
friends.remove("Jim")

print(friends.index("Poe"))
print(friends.count("Tim"))
friends.sort()
nums.sort()
print(nums)
print(friends)

friends2 = friends.copy()
print(friends2)

friends3 = friends2
friends3[2] = "Hey"
print(friends2)