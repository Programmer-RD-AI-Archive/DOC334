CREATE TABLE EMP_Table (
    EMPNO INT NOT NULL,
    ENAME VARCHAR(255),
    JOB VARCHAR(255),
    MGR CHAR(4),
    HIREDATE DATE,
    SAL INT,
    COMM INT,
    DEPTNO INT,
    PRIMARY KEY (EMPNO),
    FOREIGN KEY (DEPTNO) REFERENCES Test(DEPT_Table)
);

INSERT INTO
    EMP_Table (
        EMPNO,
        Ename,
        JOB,
        MGR,
        HIREDATE,
        SAL,
        COMM,
        DEPTNO
    )
VALUES
    (
        7369,
        'SMITH',
        'CLERK',
        7902,
        '1981-06-13',
        800,
        NULL,
        20
    ),
    (
        7499,
        'ALLEN',
        'SALESMAN',
        7698,
        '1983-07-15',
        1600,
        300,
        30
    ),
    (
        7521, 'WARD', 'JONES', 'MARTIN'
    );

CREATE TABLE DEPT_Table (
    DEPTNO INT NOT NULL,
    DNAME VARCHAR(255),
    LOC VARCHAR(255),
    PRIMARY KEY (DEPTNO)
);
