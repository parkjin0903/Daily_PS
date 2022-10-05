#include <string>
#include <vector>
#include <iostream>
using namespace std;
int cn;

bool cmp(string a, string b)
{
    if(a[cn] != b[cn]) return a[cn] < b[cn];
    return a < b;
}

#include <algorithm>

vector<string> solution(vector<string> strings, int n) {
    cn = n;
    sort(strings.begin(), strings.end(), cmp);
    return strings;
}

