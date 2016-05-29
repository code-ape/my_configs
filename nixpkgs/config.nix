{

  packageOverrides = pkgs_: with pkgs_; {
    all = with pkgs; buildEnv {
      name = "all";
      paths = [
        vim 
        wget
        htop
        tree
      ];
    };
    develop = with pkgs; buildEnv {
      name = "develop";
      paths = [
        python
        git
        leiningen
      ];
    };
  };
}
