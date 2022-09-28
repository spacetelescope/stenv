---
name: New Package request
about: Add a new package to `stenv`
title: add `<package>` to environment
labels: new package
assignees: ''

---

The default environment of `stenv` represents the "basic" software stack for work with space telescope data. If you would like to add a package to this environment, please consider the following: 

- [ ] Is the new package only useful or relevant for a small number of users?
- [ ] Does the new package require specific versions of other packages in `stenv` (i.e., would inclusion of this package introduce constraints to the requirements to older versions)?
- [ ] Do the new package's tests take a long time to complete / use large data files?

If any of the above are true, the package might not be suitable for inclusion in the base environment; however, it still might merit the creation of a separate environment focused on the package requirements.
