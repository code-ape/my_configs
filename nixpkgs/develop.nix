{
  packageOverrides = pkgs_: with pkgs_; {
    develop = with pkgs; buildEnv {
      name = "develop";
      paths = [
        git
        python
        lein
      ];
    };
  };
}
