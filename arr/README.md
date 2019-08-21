<pre>def unique(arr):
    k=0
    while k < arr.shape[0]:
        x = arr[k]
        barr = (x==arr).all(1)
        barr[np.where(barr==True)[0][0]] = False
        arr = np.delete(arr, np.where(barr==True), 0)
        k+=1
    return arr</pre>
