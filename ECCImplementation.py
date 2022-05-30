from tinyec import registry
import secrets

ecc_curve = registry.get_curve('secp224r1')

private_key_one = secrets.randbelow(ecc_curve.field.n)
private_key_two = secrets.randbelow(ecc_curve.field.n)

public_key_one = private_key_one * ecc_curve.g
public_key_two = private_key_two * ecc_curve.g

print("private key 1:", private_key_one)
print("private key 2:", private_key_two)

print("public key 1:", public_key_one)
print("public key 2:", public_key_two)

