#include <iostream>
using namespace std;
int partition(int arr[], int start, int end){
    int pivot = arr[end];
    int p_index = start;
    for(int i = start; i <= end - 1; i++){
        if(arr[i] <= pivot){
            swap(arr[i], arr[p_index]);
            p_index++;
            
        }
        
    }
    swap(arr[p_index], arr[end]);
    return p_index;
}
void quick_sort(int arr[], int start, int end){
    if(start < end){
    int p_index = partition(arr, start, end);
    quick_sort(arr, start, p_index - 1);
    quick_sort(arr, p_index + 1, end);
}}
int main(void){
    int arr[7] = {1, 4, 1, 2, 7, 5, 2}; 
    quick_sort(arr, 0, 6);
    for(int i = 0; i <= 6; i++){
        cout << arr[i] << " ";
    }
}
