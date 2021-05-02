# Greek Citizen ID Lookup

## Idea
This script makes use of a Greek Goverment platform for finding citizen's electoral district ([Link](https://www.ypes.gr/mathe-poy-psifizeis-forma/)).<br>
The goal is to find the matching Greek Citizen profiles.

##### Input:
- Surname in Greek (required)
- First name in Greek (2+ characters are required)
- Father's name in Greek (2+ characters or 0 for unknown)
- Minimum birthyear (required)
- Maximum birthyear (required)


## Execution
```sh
python script.py
```

## Example 1 (Find Age)

#### Input:
- Surname in Greek (required): ΑΝΤΕΤΟΚΟΥΝΜΠΟ
- First name in Greek (2+ characters are required): ΓΙΑΝΝΗΣ
- Father's name in Greek (2+ characters or 0 for unknown): ΤΣΑΡΛΣ
- Minimum birthyear (required): 1992
- Maximum birthyear (required): 1996

#### Results:
{'surname': 'ΑΝΤΕΤΟΚΟΥΝΜΠΟ', 'firstname': 'ΓΙΑΝΝΗΣ - ΣΙΝΑ ΟΥΓΚΟ', 'fathername': 'ΤΣΑΡΛΣ', 'mothername': 'ΒΕΡΑ', 'district': 'ΑΤΤΙΚΗΣ', 'birthyear': 1994}


## Example 2 (Find Father's Name)

#### Input:
- Surname in Greek (required): Σακελλαροπούλου
- First name in Greek (2+ characters are required): Αι
- Father's name in Greek (2+ characters or 0 for unknown): 0
- Minimum birthyear (required): 1956
- Maximum birthyear (required): 1956

#### Results:
{'surname': 'ΣΑΚΕΛΛΑΡΟΠΟΥΛΟΥ', 'firstname': 'ΑΙΚΑΤΕΡΙΝΗ', 'fathername': 'ΝΙΚΟΛΑΟΣ', 'mothername': 'ΑΛΙΚΗ', 'district': 'ΑΤΤΙΚΗΣ', 'birthyear': 1956}

**The above data belong to public figures, they are publicly known and thus they are not considered sensitive.<br>Use it on your own risk.**
