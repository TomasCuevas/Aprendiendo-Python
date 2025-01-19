texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(texto)
print("\n")

sub_string = texto[2:5]
print(f"[2:5] = {sub_string}")
print("\n")

sub_string = texto[2:]
print(f"[2:] = {sub_string}")
print("\n")

sub_string = texto[:5]
print(f"[:5] = {sub_string}")
print("\n")

sub_string = texto[2:10:2]
print(f"[2:10:2] = {sub_string}")
print("\n")

sub_string = texto[::3]
print(f"[::3] = {sub_string}")
print("\n")