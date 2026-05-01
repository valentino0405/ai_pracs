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

print("\nConditional Probability Table Stored Successfully")

print("\nCPT Values")
print("P(B) =", P_B)
print("P(E) =", P_E)
print("P(A|B,E) =", P_A_BE)
print("P(A|B,~E) =", P_A_BnE)
print("P(A|~B,E) =", P_A_nBE)
print("P(A|~B,~E) =", P_A_nBnE)
print("P(J|A) =", P_J_A)
print("P(J|~A) =", P_J_nA)
print("P(M|A) =", P_M_A)
print("P(M|~A) =", P_M_nA)

def joint_prob(B, E, A, J, M):
    pB = P_B if B else 1 - P_B
    pE = P_E if E else 1 - P_E

    if B and E:
        pA = P_A_BE if A else 1 - P_A_BE
    elif B and not E:
        pA = P_A_BnE if A else 1 - P_A_BnE
    elif not B and E:
        pA = P_A_nBE if A else 1 - P_A_nBE
    else:
        pA = P_A_nBnE if A else 1 - P_A_nBnE

    if A:
        pJ = P_J_A if J else 1 - P_J_A
    else:
        pJ = P_J_nA if J else 1 - P_J_nA

    if A:
        pM = P_M_A if M else 1 - P_M_A
    else:
        pM = P_M_nA if M else 1 - P_M_nA

    return pB * pE * pA * pJ * pM

print("\nSample Query")
print("Alarm sounded but no burglary, no earthquake, John and Mary called")
result = joint_prob(False, False, True, True, True)
print("Probability =", result)

print("\nEnter 5 Queries")
for i in range(5):
    print("\nQuery", i + 1)
    B = bool(int(input("Burglary occurred? (1/0): ")))
    E = bool(int(input("Earthquake occurred? (1/0): ")))
    A = bool(int(input("Alarm sounded? (1/0): ")))
    J = bool(int(input("John called? (1/0): ")))
    M = bool(int(input("Mary called? (1/0): ")))
    ans = joint_prob(B, E, A, J, M)
    print("Joint Probability =", ans)

"""
Input:
Enter events (Example: B E A J M): B E A J M

Enter Prior Probabilities
P(Burglary): 0.001
P(Earthquake): 0.002

Enter Alarm Conditional Probabilities
P(A|B,E): 0.95
P(A|B,~E): 0.94
P(A|~B,E): 0.29
P(A|~B,~E): 0.001

Enter Call Probabilities
P(J|A): 0.90
P(J|~A): 0.05
P(M|A): 0.70
P(M|~A): 0.01

Query 1
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 1
Mary called? (1/0): 0

Query 2
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 1
Alarm sounded? (1/0): 1
John called? (1/0): 0
Mary called? (1/0): 0

Query 3
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 0
Mary called? (1/0): 0

Query 4
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 1
Mary called? (1/0): 0

Query 5
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 0
Mary called? (1/0): 1

Output:
Enter events (Example: B E A J M): B E A J M

Events in the Network:
B
E
A
J
M

Enter Prior Probabilities
P(Burglary): 0.001
P(Earthquake): 0.002

Enter Alarm Conditional Probabilities
P(A|B,E): 0.95
P(A|B,~E): 0.94
P(A|~B,E): 0.29
P(A|~B,~E): 0.001

Enter Call Probabilities
P(J|A): 0.90
P(J|~A): 0.05
P(M|A): 0.70
P(M|~A): 0.01

Conditional Probability Table Stored Successfully

CPT Values
P(B) = 0.001
P(E) = 0.002
P(A|B,E) = 0.95
P(A|B,~E) = 0.94
P(A|~B,E) = 0.29
P(A|~B,~E) = 0.001
P(J|A) = 0.9
P(J|~A) = 0.05
P(M|A) = 0.7
P(M|~A) = 0.01

Sample Query
Alarm sounded but no burglary, no earthquake, John and Mary called
Probability = 0.0006281112599999999

Enter 5 Queries

Query 1
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 1
Mary called? (1/0): 0
Joint Probability = 0.00026919054

Query 2
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 1
Alarm sounded? (1/0): 1
John called? (1/0): 0
Mary called? (1/0): 0
Joint Probability = 1.73826e-05

Query 3
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 0
Mary called? (1/0): 0
Joint Probability = 2.9910059999999997e-05

Query 4
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 1
Mary called? (1/0): 0
Joint Probability = 0.00026919054

Query 5
Burglary occurred? (1/0): 0
Earthquake occurred? (1/0): 0
Alarm sounded? (1/0): 1
John called? (1/0): 0
Mary called? (1/0): 1
Joint Probability = 6.979013999999998e-05
"""