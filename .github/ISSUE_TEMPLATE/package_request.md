---
name: Package request 
about: Add a new package to `stenv`
title: add `<package>` to environment 
labels: new package 
assignees: ''

---

<!-- Feel free to modify this placeholder text to be relevant to your request: -->
`<package>` should be added to the base `stenv` environment.

<!-- The default environment of `stenv` represents the "basic" software stack for work with space telescope data. If you
would like to add a package to this environment, please consider the following: -->
- [ ] This package is useful or relevant to a significant amount of `stenv` users.
- [ ] This package does not require specific versions of other packages in `stenv` (inclusion would not introduce
  significant backward constraints to the requirements).
- [ ] This package's tests do not take an overly long time to complete, and test data files are not significantly large.

<!-- If any of the above are not true, this package might not be suitable for inclusion in the base environment; 
however, it still might merit the creation of a separate environment focused on the specific package requirements. -->
