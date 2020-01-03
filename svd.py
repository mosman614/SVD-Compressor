import numpy as np
import imageio;
import matplotlib.pyplot as plt

img_url = "pb.jpg"
# import os
# b = os.path.getsize(img_url)


from tempfile import TemporaryFile
outfile = TemporaryFile()



def compres(filename):
	A=imageio.imread(filename);


	A=np.double(A); 
	A=A-np.mean(A);
	orig_len = A.shape
	orig_dim1 = A.shape[0]
	orig_dim2 = A.shape[1]
	

	if (len(A.shape)==3):
		if (A.shape[2] == 4):
			A = A[:,:,:3]
		A = A.reshape(orig_dim1,orig_dim2*3)

	U, S, V = np.linalg.svd(A)
	svdd = np.flip(np.sort(S))

	percent_var = 0.

	sv_kept = 1
	while (percent_var < .95):
		percent_var = np.sum(svdd[:sv_kept]**2)/(np.sum(svdd**2))
		sv_kept += 1



	U_recon = U[:,0:sv_kept]
	V_recon = V[0:sv_kept,:]
	S_recon = S[:sv_kept]
	np.save('T', np.array([U_recon, V_recon, S_recon]))


	A_recon = U_recon@np.diag(S_recon)@V_recon

	if (len(orig_len) == 3):
		A_recon = A_recon.reshape(orig_dim1, orig_dim2, 3)


	flname = filename+'compressed.jpg'
	
	c = imageio.imwrite(flname, A_recon)

	return flname

compres(img_url)
# R = compres(A.reshape(A.shape[0],A.shape[1]*3))



# img_recon = R.reshape(600,900,3)

# c = imageio.imwrite(img_url + 'compressed.jpg', img_recon)
# d = os.path.getsize('astronaut-gray.jpg')

# reduction = (b-d)/d

# print("Your file has been reduced by {} percent".format(reduction*100))
# print()
# print("Your reconstruction loss is {}".format(np.abs(np.sum(img_recon**2) - np.sum(A**2))/(np.sum(A**2))))
# fig,ax = plt.subplots(1,2,figsize=(15,7))
# ax[1].imshow(A)
# ax[1].set_title('Before Compression')
# ax[0].imshow(img_recon)
# ax[0].set_title('After Compression')

# plt.show()


