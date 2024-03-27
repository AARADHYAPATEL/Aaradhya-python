

def test(nums):
    return ["A+" if grade >= 4.0
            else ("A" if grade >= 3.7
                  else ("A-" if grade >= 3.4
                        else ("B+" if grade >= 3.0
                              else ("B" if grade >= 2.7
                                    else ("B-" if grade >= 2.4
                                          else ("C+" if grade >= 2.0
                                                else ("C" if grade >= 1.7
                                                      else ("C-" if grade >= 1.4
                                                            else "F"))))))))
            for grade in nums]

   
nums = [4.0, 3.5, 3.8]
print("List of numbers:",nums)
print("Convert GPAs to letter grades:")
print(test(nums))
nums = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
print("\nList of numbers:",nums)
print("Convert GPAs to letter grades:")
print(test(nums))

