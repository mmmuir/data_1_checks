# Generate every common rendering of a given a standard American full name (first, middle, last) and most frequently used nickname.
# Output format includes Google search query syntax.
# For use only in consentful doxx-defense inquiries. For more on doxx-defense, see https://emmibevensee.com/?p=662
def permutate():
    fullname = input('Type in your full name:')
    nname = input('Type in your nickname:')
    fname, mname, lname = fullname.split(' ')
    minit = mname[0]
    fullname_permutations = f"\"{fname} {mname} {lname}\"|\"{fname} {minit} {lname}\"|\"{nname} {mname} {lname}\"|\"{nname} {minit} {lname}\"|\"{fname} {lname}\"|\"{nname} {lname}\"|\"{lname} {fname} {mname}\"|\"{lname} {fname} {minit}\"|\"{lname} {nname} {mname}\"|\"{lname} {nname} {minit}\"|\"{lname} {fname}\"|\"{lname} {nname}\""
    print(fullname_permutations)

permutate()
