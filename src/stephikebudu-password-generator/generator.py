import string, random

def generator():
  lower_letters = list(string.ascii_lowercase)
  upper_letters = list(string.ascii_uppercase)
  nums = list(string.digits)
  chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "{", "[", "}", "]", "|", "\\", ":", ";", '"', "'", "<", ">", ".", "?", "/"]

  def get_random_el(li):
    random_idx = random.randint(0, (len(li) - 1))
    return li[random_idx]

  def get_random_list():
    return get_random_el([lower_letters, upper_letters, nums, chars])

  password = f"{get_random_el(upper_letters)}{get_random_el(lower_letters)}{get_random_el(chars)}{get_random_el(nums)}"
  while len(password) < 8:
    password += get_random_el(get_random_list())

  return f"Your new password is {password}"

print(generator())