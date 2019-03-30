count=1
for i = 0:63

    myfilename = sprintf('Empty/opencv_frame_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 0;
    count = count + 1;
            
        
end
for i = 0:63

    myfilename = sprintf('White Bishop/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 1;
    count = count + 1;
            
        
end
for i = 0:63

    myfilename = sprintf('White King/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 2;
    count = count + 1;
            
        
end
for i = 0:63

    myfilename = sprintf('White Knight/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 3;
    count = count + 1;
            
        
end
for i = 0:63

    myfilename = sprintf('White Pawn/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 4;
    count = count + 1;
            
        
end
for i = 0:63

    myfilename = sprintf('White Queen/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 5;
    count = count + 1;
            
        
end
for i = 0:63

    myfilename = sprintf('White Rook/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 6;
    count = count + 1;
            
        
end
for i = 1:64

    myfilename = sprintf('Yellow Bishop/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 7;
    count = count + 1;
            
        
end
for i = 1:64

    myfilename = sprintf('Yellow King/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 8;
    count = count + 1;
            
        
end
for i = 1:64

    myfilename = sprintf('Yellow Knight/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 9;
    count = count + 1;
            
        
end
for i = 1:64

    myfilename = sprintf('Yellow Pawn/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 10;
    count = count + 1;
            
        
end
for i = 1:64

    myfilename = sprintf('Yellow Queen/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 11;
    count = count + 1;
            
        
end
for i = 1:64

    myfilename = sprintf('Yellow Rook/opencv_frame1_%d.jpg', i);
    img = imread(myfilename);
    [height, width, dim] = size(img);
    X(:,:,:,count) = img;                
    Y(count,1) = 12;
    count = count + 1;
            
        
end
save('chess_train_final.mat','X','Y');
