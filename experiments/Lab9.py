import re
# Define expert system rules
rules = {
    'cough': {
        'bronchitis': 0.8,
        'pneumonia': 0.7,
        'asthma': 0.4
    },
    'fever': {
        'flu': 0.9,
        'pneumonia': 0.7,
        'bronchitis': 0.4
    },
    'fatigue': {
        'flu': 0.8,
        'pneumonia': 0.6,
        'asthma': 0.3
    },
    'shortness of breath': {
        'pneumonia': 0.9,
        'asthma': 0.6,
        'bronchitis': 0.3
    }
}

# Define function to prompt user for symptoms and return diagnosis
def diagnose():
    # Prompt user for symptoms
    symptoms = input('Enter your symptoms (comma-separated): ').split(',')
    
    # Initialize diagnosis dictionary
    diagnosis = {}
    
    # Iterate through rules to infer diagnosis
    for symptom in symptoms:
        if symptom in rules:
            for condition, score in rules[symptom].items():
                if condition not in diagnosis:
                    diagnosis[condition] = score
                else:
                    diagnosis[condition] *= score
    
    # Normalize scores and sort by descending score
    total = sum(diagnosis.values())
    diagnosis = {condition: score/total for condition, score in diagnosis.items()}
    diagnosis = sorted(diagnosis.items(), key=lambda x: x[1], reverse=True)
    
    # Print diagnosis
    print('\nDiagnosis:')
    for condition, score in diagnosis:
        print('- {} ({:.1%} chance)'.format(condition, score))

# Run expert system
diagnose()
Enter your symptoms (comma-separated): fever,cough,fatigue

'''Diagnosis:
- flu (49.5% chance)
- bronchitis (22.0% chance)
- pneumonia (20.2% chance)
- asthma (8.3% chance)'''
