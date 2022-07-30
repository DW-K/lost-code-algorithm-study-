#include<iostream>

using namespace std;

const int MAX_SIZE = 50;
int N, M;

int result = 0;
long long truth = 0;
long long attend_table[MAX_SIZE];
int visit_table[MAX_SIZE];

void dp() {
    int input_count, temp;
    cin >> N >> M;
    result = M;
    cin >> input_count;

    for (int i = 0; i < input_count; ++i) {
        long long num = 1;
        cin >> temp;
        truth += (num << (temp-1));
    }

    for (int i = 0; i < M; ++i) {
        cin >> input_count;
        for (int j = 0; j < input_count; ++j) {
            long long num = 1;
            cin >> temp;
            attend_table[i] += (num << (temp-1));
        }
    }

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < M; ++j) {
            if(visit_table[j] == 1) continue;

            if(visit_table[j] == 0 && (truth & attend_table[j]) > 0) {
                result--;
                visit_table[j] = 1;
                truth = truth | attend_table[j];
            }
        }
    }

    cout << result << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    dp();
}
