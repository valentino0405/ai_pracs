events = input("Enter events (Example: B E A J M): ").split()

print("\nEvents in the Network:")
for e in events:
    print(e)

print("\nEnter Prior Probabilities")
P_B = float(input("P(Burglary): "))
P_E = float(input("P(Earthquake): "))

print("\nEnter Alarm Conditional Probabilities")
P_A_BE = float(input("P(A|B,E): "))
P_A_BnE = float(input("P(A|B,~E): "))
P_A_nBE = float(input("P(A|~B,E): "))
P_A_nBnE = float(input("P(A|~B,~E): "))

print("\nEnter Call Probabilities")
P_J_A = float(input("P(J|A): "))
P_J_nA = float(input("P(J|~A): "))
P_M_A = float(input("P(M|A): "))
P_M_nA = float(input("P(M|~A): "))

print("\n--- CPT Stored Successfully ---")

def joint_prob(B, E, A, J, M):
    pB = P_B if B else (1 - P_B)
    pE = P_E if E else (1 - P_E)

    if B and E:
        pA = P_A_BE if A else (1 - P_A_BE)
    elif B and not E:
        pA = P_A_BnE if A else (1 - P_A_BnE)
    elif not B and E:
        pA = P_A_nBE if A else (1 - P_A_nBE)
    else:
        pA = P_A_nBnE if A else (1 - P_A_nBnE)

    if A:
        pJ = P_J_A if J else (1 - P_J_A)
    else:
        pJ = P_J_nA if J else (1 - P_J_nA)

    if A:
        pM = P_M_A if M else (1 - P_M_A)
    else:
        pM = P_M_nA if M else (1 - P_M_nA)

    return pB * pE * pA * pJ * pM

print("\nSample Query:")
print("Alarm = True, B = False, E = False, J = True, M = True")

result = joint_prob(False, False, True, True, True)
print("Probability =", result)

print("\nEnter 5 Queries:")

for i in range(5):
    print("\nQuery", i + 1)

    B = bool(int(input("Burglary (1/0): ")))
    E = bool(int(input("Earthquake (1/0): ")))
    A = bool(int(input("Alarm (1/0): ")))
    J = bool(int(input("John (1/0): ")))
    M = bool(int(input("Mary (1/0): ")))

    ans = joint_prob(B, E, A, J, M)
    print("Joint Probability =", ans)