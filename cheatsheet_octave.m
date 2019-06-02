% mathematical operations that we can do
5 + 6 				% return 11
3 -2  				% return 1
1 / 2 				% return 0.50000
2^6 				% return 64

% boolean  and logic commands can be used as

1 == 2 				% as this condition is false, so answer we get will be 0
1 ~= 2 				%  as this condition is true, ( '~' for not equal) so answer we get will be 1
1 && 0 				% AND, will return 0
1 || 0 				% OR, will return 1
xor(1,0)			% return 1

PS('>> '); 			% to change the prompt to provided string in '' quotes

a = 3
b = 'string'
c = ( 3 >= 1)  							% return c value as 1
a = pi; 								% putting value of a as 3.1416
disp(a);								% DISPLAYS value of a
disp(sprintf('2 decimals : %0.2f',a)) 	% displays -> 2 decimals : 3.14
disp(sprintf('2 decimals : %0.6f',a)) 	% displays -> 2 decimals : 3.141593

format long 							% sets default datatype as long
disp(a)									% displays a as 3.14159265358979, due to setted as long
format short							% sets default datatype as short
disp(a)									% displays a as 3.1416, due to setted as short

A = [ 1 2; 3 4; 5 6]  				% creates a 3 * 2 matrix  and print out the result
A = [ 1 2; 3 4; 5 6]; 				% using the ';' will not print the output of the command
v = [1 2 3] 						% creates a row vector 1 * 3
v = [1 ; 2 ; 3] 					% creates a column vector 3 * 1
v = 1: 0.1 : 2 						% creates a row from 1-2 ( both limits INCLUDED) with elements incremented by 0.1
v = 1:6 							% creates a row [ 1 2 3 4 5 6] ( both limits INCLUDED)
ones(2,3) 							% generate 2 * 3 matrix with values 1 each
zeros(1,3) 							% generate 1 * 3 matrix with values 0 each
w = rand(1,3)						% generate 1 * 3 matrix with values between  0 - 1 each 
									% or from gausian distribution with mean 0 and standard deviation 1 (+ve side)
v = randn(1,3)						% generate 1 * 3 matrix with values between -1 - 0 each
									% or from gausian distribution with mean 0 and standard deviation 1 (-ve side)

w = -6 + sqrt(10)*(randn(1,10000)); % generate a 10,000 size vector with mean -6
hist(w)								% generate histogram
hist(w,50) 							% generate histogram with bin size = 50
help eye 							% give details regarding 'eye' command, work for other commands too

%------------------------------
size(A)             			% gives dimensions of A i.e. 3 2
length(v) 						% gives dimension value of v, 
length(A) 						% gives value of longest dimension i.e. 3


pwd 							% gives current path or directory
cd 'address' 					% helps to go to that 'address' specified directory
ls 								% same as that of linux command, gives details about current directory
load('qwerty.dat') 				% helps in loading the file data 'qwerty.dat' in variable 'qwerty'
who 							% gives info about all variables present in octave memory
whos							% gives info about all variables present in octave memory, 
								% along with all details about specific variable
clear 'variable name' 			% clear the variable from memory
clear							% clear all variables from memory
v = qwerty(1:10) 				% assign ten values ( from top ) to 'v'
save hello.mat v 				% save variable 'v' in hello.mat (in binary format)
save hello.txt v -ascii 		% save as text(ASCII)
load hello.mat 					% loading data from file


A(3,2) 							% returns value at '3' row and '2' column i.e. 6
A(2,:)							% returns all value from second row i.e 3 4
A(:,2) 							% returns all value from second column i.e. 2 4 6
A([1 3], :) 					% get every column from row '1','3'
A(:,2) = [10 ; 11 ; 12] 		% assigning new value to that specific column
A = [A , [13 ; 14 ; 15]] 		% append another column to A, making it 3 * 3 matrix
A(:) 							% putting all values present in the matrix in single column matrix
C = [ A B ] 					% concatenating two matrices row wise i.e. no of columns changes
C = [ A , B] 					% (same as above)
C = [A ; B] 					% concatenating two matrices column wise i.e. no of rows changes

%-----------------------------------------

A * D 							% returns their matrix multiplication
A .* B 							% returns element wise multiplication
A .^ 2 							% returns square of elements of A
1 ./ A 							% returns element wise inverse of A
log(v) 							% returns element wise log values of v
exp(v) 							% returns exxponential values, element wise of v
abs(v)							% returns absolute values of v, element wise
-v 								% same as -1*v
v + ones(length(v),1) 			% increments element values of v by 1
v + 1							% ( same as above)
A' 								% returns transpose of A
q = max(a)                      % returns maximum value out of 'a'
[q , ind] = max(a)              % returns maximum value out of 'a' and its position
max(A) 							% returns column wise maximum values, i.e. 5 6
a = [ 1 15 2 0.5 ]
a < 3 							% will consider and return if it is true for all elements, i.e. 1 0 1 1
find(a <4) 						% will consider and return for all element's indices for which it is true, i.e. 1 3 4
magic(3) 						% will give a magic square, where sum of elements in row, column and diag are equal
[r,c] = find( A >=7 ) 			% will return row in r, and column in c, for elements satisfying condition
								% here for A = [8 1 6;	3 5 7;	4 9 2] it will give r = [1;3;2] and c= [1;2;3]
sum(a) 							% return the sum of all elements of a
prod(a) 						% return the product of all elements of a
floor(a) 						%round down number to nearest integer
ceil(a) 						%round up number to nearest integer
max( rand(3) , rand(3)) 		% create a 3*3 matrix whose elements are selected from 2 other randomly generated
								% and pick maximum from them, element wise,
max( A,[],1) 					% select max values from first dimension of A i.e. row 
								% % here for A = [8 1 6;	3 5 7;	4 9 2] it will return 8 9 7
max( A,[],2) 					% select max values from second dimension of A i.e. column 
								% % here for A = [8 1 6;	3 5 7;	4 9 2] it will return 8 ; 7;  9
max(max(A))						% return max value in all elements i.e. 9
max(A(:))						% (same as above)
sum ( magic(9),1)				% sum of all row elements in 9*9 magic square, column wise i.e. 369 369 369 369 369 369 369 369 369
sum ( magic(9),2)				% sum of all column elements in 9*9 magic square, row wise i.e. 369; 369; 369; 369; 369; 369; 369; 369; 369
sum(sum(A.*eye))				% sum of all elements of diag(A), which is obtained by 
								% element wise multiplication of identity matrix i.e. it returns 369
flipud(eye(2))					% flip matrix, up side down, i.e it will return [0 1;1 0]
pinv(A)							% returns pseudo inverse of A ( equal to proper inverse for square matrix)


%---------------------------------------------------------------

t = [0:0.01:0.98];
y1 = sin(2*pi*4*t);
plot(t,y1); 					% plotting the input v.s. output of function
hold on;						% fixes previous figure, and then we plot on it more figures
y2 = cos(2*pi*4*t);
plot(t,y2,'r');					% 'r' for red colour
xlabel('time');					% setting x label of graph
ylabel('value');				% setting y label of graph
legend('sin', 'cos')			% for setting legends for figure
title('my plot')				% for setting plot of graph
print -dpng 'filename.png'      % saving figure with given string as file name
close 							% disappears figure;

% for plotting figures differently
figure(1) ; plot(t,y1); 		% this helps in naming the figure as 'figure 1' and 'figure 2'
figure(2) ; plot(t,y2);

% for sub plotting , i.e. two or more graphs in same figure
subplot(1,2,1); 				% Divides plot a 1*2 grid, access first element
plot(t,y1);
subplot(1,2,2);					% now accessing second element
plot(t,y2);
axis([0.5 1 -1 1]) 				% sets boundaries of x axis as (0.5,1) and y axis as (-1,1)
clf;							% clears the figure

% using A = magic square 5*5
imagesc(A) 						% plot a grid of colours in which each color coresponds to different value of matrix
imagesc(A), colorbar, colormap grey;
								% runnung three commands at a time, colorbar give scale for color changing,
								% colormap grey uses to differen shades of 'grey' color for mapping different values
a = 1 , b = 2 , c = 3; 			% running different commands at same time


%--------------------------------------------------------------
% using v = zeros(10,1)
for i = 1:10, 					% using for loop
	v(i) = 2^i;					% i.e. 2; 4; 8; 16; 32; 64; 128; 256; 512; 1024;
end;

indices = 1:10; 				% using for loop
for i = indices, 				% i.e. 1; 2; 3; 4; 45; 6; 7; 8; 9; 10;
	disp(i);
end;

i = 1;
while i<= 5,					% using while loop
	v(i) = 100;					% after loop ends, it returns v as 100; 100; 100; 100; 100; 64; 128; 256; 512; 1024;
	i = i+1;
end;

i =1;
while true,						% using while loop
	v(i) = 999; 				% after loop ends, it returns v as 999; 999; 999; 999; 999; 64; 128; 256; 512; 1024;
	i = i +1;
	if i == 6,
		break;
	end;
end;

v(1) = 2;
if v(1) == 1, 					% using conditional statements 'if','elseif' and 'else'
	disp('first case statement, if holds true');
elseif v(1) == 2,
	disp('second case statement, if holds true');
else
	disp('default');
end;

quit 							% for closing octave

% USING FUNCTIONS IN OCTAVE:

% like the functions should be made in different file like 'squareThisNumber.m'
function y = squareThisNumber(x) 
y = x^2; 						% commands used inside the function file 'squareThisNumber.m'
squareThisNumber(5) 			% calling the function, note : the function should be in same directory as file
								% i.e. will give 25

% like the functions should be made in different file like 'squareAndCubeThisNumber.m'
function [y1,y2] = squareAndCubeThisNumber(x) 
y1 = x^2;
y2 = x^3;
[a,b] = squareAndCubeThisNumber(5) % calling this will give a =25, b=125

% Octave search path
addpath('my string') 			% will add the address in octave searching, so that whenever it searches
								% it searches in 'my string' as well.
