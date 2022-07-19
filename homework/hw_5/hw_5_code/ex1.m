% 1.2
X = randi([0 100000], 1000, 100);

% 1.2.a
tic
svd(X);
toc

% 1.2.b
tic
svd(X');
toc

% 1.2.c
tic
eig(X * X');
toc

% 1.2.d
tic
eig(X' * X);
toc

% 1.3.a
X = [-9 11 -21 63 -252;
    70 -69 141 -421 1684;
    -575 575 -1149 3451 -13801;
    3891 -3891 7782 -23345 93365;
    1024 -1024 2048 -6144 24572];

err_eig = zeros(5, 1);
eig_X = eig(X);

for i = 1:1000
    dX = eps(X);
    err_eig = err_eig + eig(X + dX) - eig_X;
end

err_eig

% 1.3.b
sum_dX = zeros(5, 5);
err_sin = zeros(5, 1);
svd_X = svd(X);

for i = 1:1000
    dX = eps(X);
    err_sin = err_sin + svd(X + dX) - svd_X;
end

err_sin
