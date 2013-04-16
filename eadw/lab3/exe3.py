

def preRecF1(set_of_Documents, set_relevant_IDs):
    
    precision = float(len(set_of_Documents.intersection(set_relevant_IDs))) / float(len(set_of_Documents))
    recall = float(len(set_of_Documents.intersection(set_relevant_IDs)))/float(len(set_relevant_IDs))
    
    if(precision + recall) > 0:
        F1 = 2 * (precision * recall) / (precision + recall)
    else:
        F1 = 0
    return precision, recall, F1


print preRecF1(set([152, 15]), set([152, 80 ,66]))