#ifndef FUNC
#define FUNC

#include <bits/stdc++.h>

using namespace std;

class Solution
{
private:
    vector<vector<double>> A;
    vector<double> b;
    vector<double> y;
    vector<double> zero;

public:
    Solution(int n);
    ~Solution(){};

    void GaussEliminationWithPivoting(double epsilon);
    void GaussSeidelIteration(double epsilon);
    bool JudgeIteration(vector<double> x1, vector<double> x0, double e);
    void InitMatrix(double down, double mid, double up);
    void InitVector(double value);
    double Distance(vector<double> x1, vector<double> x0);
    void AccuRes(double epsilon);
};

#endif