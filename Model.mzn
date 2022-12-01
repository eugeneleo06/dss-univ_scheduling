include "globals.mzn";
include "data_source.dzn";

% DOSEN
enum dosen;

% MATA KULIAH
enum matkul;

% HARI
enum hari;

% Hubungan Dosen x Matkul
array [int, int] of int : dosen_matkul;

% Hubungan Dosen x Hari
array [int, int] of int : dosen_hari;

% Output Variable
array [dosen, matkul, hari] of var 0..1 : solution;


constraint % general and logical
  forall (i in dosen) (
    forall (j in matkul) (
      forall (k in hari) (
          solution[i, j, k] >= 0 /\ solution[i, j, k] <= 1
          /\
          solution[i, j, k] <= dosen_matkul[i, j] 
          /\
          solution[i, j, k] <= dosen_hari[i,k]
      )
    )
  );
  
constraint % dalam 1 hari dosen hanya boleh ngajar 1 matkul
  forall(k in hari) ( 
      sum(i in dosen, j in matkul)(solution[i,j,k]) <= 1
  );

constraint % matkul harus diajar
  forall(j in matkul) ( 
      sum(i in dosen, k in hari)(solution[i,j,k]) == 1
  );

solve satisfy;

output [show(solution[i,j,k]) ++
        " " ++ show(i) ++ " " ++ show(j) ++ " " ++ show(k) ++ "\n" 
        ++
        if k == max(index_set(hari)) 
          then "\n" 
        endif
        |
        i in dosen,
        j in matkul,
        k in hari
];
