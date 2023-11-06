#include <map>
#include <iostream>
#include <random>
#include <vector>
#include <tuple>
#include <ctime>
#include <fstream>
using namespace std;


tuple<double, double> InsertionTesting (multimap<int, int> bmap, unordered_map<int, int> hmap, vector<tuple<int, int>> &ary , int n, int ary_size)
{
    // Insert into Multimap
    std::clock_t start_time = std::clock();
    for (int i = 0; i < n ; i++)
    {
        bmap.insert(pair<int,int> (get<0>(ary.at(i % ary_size)), get<1>(ary.at(i % ary_size))));
    }
    std::clock_t temp_bmap = std::clock() - start_time;

    double tot_time = ((double) temp_bmap) / (double) CLOCKS_PER_SEC;

    // Insert into Unordered Map
    std::clock_t start_time_map = std::clock();
    for (int i = 0; i < n; i++)
    {
        hmap.insert(pair<int,int> (get<0>(ary.at(i % ary_size)), get<1>(ary.at(i % ary_size))));
    }
    std::clock_t temp_hmap = std::clock() - start_time_map;

    double tot_time_map = ((double) temp_hmap) / (double) CLOCKS_PER_SEC;

    return make_tuple(tot_time, tot_time_map);
}


vector<tuple<int, int>> GenerateRandomInputArray(int n)
{
    vector<tuple<int, int>> res;

    for (int i = 0; i < n ; i++)
    {
        // cout << rand() % 100 << endl;
        tuple<int, int> x = make_tuple(rand() % n, rand() % n);
        res.push_back(x);
    }

    return res;
}




/**
 * Main Function
*/
int main() 
{
    multimap<int, int> bmap;
    unordered_map<int, int> hmap;

    int ary_size = 100000;

    std::ofstream myfile;
    myfile.open("results.csv");

    myfile << "Size" << "Binary Map" << "," << "Hash Map" << "\n";
    
    vector<tuple<int, int>> ary = GenerateRandomInputArray(ary_size);
    tuple<double, double> tup = InsertionTesting(bmap, hmap, ary, 50000, ary_size);
    myfile << get<0>(tup) << "," << get<1>(tup) << "\n";

    int n = 100000;
    while (get<0>(tup) < 3 && get<1>(tup) < 3)
    {
        multimap<int, int> bmap;
        unordered_map<int, int> hmap;
        tup = InsertionTesting(bmap, hmap, ary, n, ary_size);
        myfile << n << "," << get<0>(tup) << "," << get<1>(tup) << "\n";
        n += 50000;
        cout << get<0>(tup) << endl;
    }

    myfile.close();

    return 0;
}