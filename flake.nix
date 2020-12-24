{
  inputs.nixpkgs.url = github:NixOS/nixpkgs/20.09;

  outputs = { self, nixpkgs }:
  let
    supportedSystems = [ "x86_64-linux" "x86_64-darwin" ];
    forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);
  in
    {
      defaultPackage = forAllSystems (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};

          texsoup = pkgs.python3Packages.buildPythonPackage rec {
              pname = "texsoup";
              version = "0.3.1";
              name = "${pname}-${version}";
              src = builtins.fetchurl {
                url = "https://files.pythonhosted.org/packages/84/58/1c503390ed1a81cdcbff811dbf7a54132994acef8dd2194d55cf657a9e97/TexSoup-0.3.1.tar.gz";
                sha256 = "02xpvmhy174z6svpghzq4gs2bsyh0jxc2i7mark8ls73mg82lsrz";
              };
              doCheck = false;
            };
        in
          pkgs.python3Packages.buildPythonPackage rec {
            name = "removesoln";
            src = ./.;
            propagatedBuildInputs = [ texsoup ];
          }
      );

    };

}
