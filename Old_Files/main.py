from Template_Decision import *
from libraries_btTDD import *

         
#truth_table = np.array([[1,1,1],[0,2,1],[0,1,2]])
#truth_table = np.array([[0,2,1],[1,1,1],[0,2,1]])
#truth_table = np.array([[0,1,1],[0,1,1],[0,1,1]])

#truth_table = np.array([[0,1,2],[1,2,0],[2,0,1]]) #HA

#truth_table = np.array([[0,1,2],[0,1,2],[0,1,2]])

#truth_table = np.array([[0,1,2],[1,2,0],[1,2,0]])

#truth_table = np.array([[1,1,1],[1,1,1],[1,1,1]])

## FA1 Sum: 24 + 12 = 36,
#truth_table = np.array([[0,1,2],[1,2,0],[2,0,1]])
#truth_table = np.array([[1,2,0],[2,0,1],[0,1,2]])
#C0
#truth_table = np.array([[0,0,0],[0,0,0],[0,1,1]])
#truth_table = np.array([[0,0,1],[0,1,1],[1,1,1]])
truth_table = np.array([[0,1,1],[1,1,1],[1,1,2]])

print "Truth Table"
print "   0  1  2"
print "------------"
print "0| %d  %d  %d" %(truth_table[0,0],truth_table[0,1],truth_table[0,2])
print "1| %d  %d  %d" %(truth_table[1,0],truth_table[1,1],truth_table[1,2])
print "2| %d  %d  %d\n" %(truth_table[2,0],truth_table[2,1],truth_table[2,2])

out_btTdd,null = decision_template(truth_table)

cost_vector,tc,init_cost_table = transistor_count(out_btTdd)

print_btTDD(out_btTdd)

