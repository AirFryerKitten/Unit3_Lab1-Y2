#Jonas York
#
#

def sample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    sample(num-1)
    print(f"Returning; num = {num}")
    return


def loopsample(num):
  print()
  othernum = num
  while num != 0:
    print(f"Recursing; num = {num}")
    num-=1
  print("\nBASE CASE REACHED\n")
  while num < othernum:
    print(f"Returning; num = {num+1}")
    num+=1



def main():
  num = 5
  sample(num)
  loopsample(num)

if __name__ == "__main__":
  main()
