import numpy as np
from numpy import linalg as lg

#diberikan beberapa judul buku sebagai berikut
#d1=Algoritma Pemrograman
#d2=Pemrograman Java
#d3=Algoritma Lanjut
#d4=Pemrograman Basis Data
#d5=Matematika Diskrit
#d6=Basis Data Relasional


#inisiasi matrix A, dokumen dan kata
A=np.matrix([[1,0,1,0,0,0],[1,1,0,1,0,0],[0,1,0,0,0,0]
             ,[0,0,1,0,0,0],[0,0,0,1,0,1],[0,0,0,0,1,0]
             ,[0,0,0,0,0,1]])

#mencari komponen matrix A=u dot s dot vh
u, s, vh = np.linalg.svd(A, full_matrices=True)

#asumsi k=2
u=u[:,:2]   #mengubah matrix u menjadi matrix 7 x 2
vh=vh[:2,:] #mengubah matrix vh menjadi matrix 2 x 6

#membuat matrix diagonal
sigma = np.diag(s)
#asumsi k = 2
sigma=sigma[:2,:2] #mengubah matrix sigma menjadi 2 x 2

#menghitung posisi kata "Algoritma"
Algoritma=np.dot(u[0],sigma)

#menghitung posisi kata "Pemrograman"
Pemrograman=np.dot(u[1],sigma)

#menghitung posisi kata "Algoritma Pemrograman"
#dengan cara (posisi algoritma+posisi pemrograman)/2
algoritma_pemrograman=(Algoritma+Pemrograman)/2
#transpose matrix algoritma pemrograman agar dapat 
#menghasilkan dot product dengan dokumen
algoritma_pemrograman=algoritma_pemrograman.transpose()

#menghitung posisi tiap dokumen
dokumen=np.dot(sigma,vh)
#transpose matrix dokumen agar dapat menghasilkan dikalikan(dot product)
#dengan algoritma_pemrograman
dokumen=dokumen.transpose()
