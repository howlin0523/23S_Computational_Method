#include <bits/stdc++.h>
#include "func.h"
#include "func.cpp"

using namespace std;

int main()
{
    Solution solution = Solution(100);
    vector<double> epsilons{1.0, 0.1, 0.01, 0.0001};
    int n = 100;
    double h = (double) 1 / n;
    for (auto epsilon : epsilons)
    {
        cout << "epsilon :" << epsilon << endl;
        solution.AccuRes(epsilon);
        solution.InitMatrix(epsilon, -(2 * epsilon + h), epsilon + h);
        solution.GaussEliminationWithPivoting(epsilon);
        cout << "epsilon :" << epsilon << endl;
        solution.InitMatrix(epsilon, -(2 * epsilon + h), epsilon + h);
        solution.GaussSeidelIteration(epsilon);
    }
    return 0;
}