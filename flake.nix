{
  description = "Star Wars ASCII film animation player and updater";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };

        python = pkgs.python3.withPackages (pypkgs: [ pypkgs.requests ]);

        mkScript =
          name: file:
          pkgs.writeShellApplication {
            inherit name;
            runtimeInputs = [ python ];
            text = ''
              exec ${python}/bin/python ${./.}/${file} "$@"
            '';
          };
      in
      {
        packages = {
          default = mkScript "starwars" "player.py";
          update = mkScript "starwars-update" "updater.py";
        };

        apps = {
          default = {
            type = "app";
            program = "${self.packages.${system}.default}/bin/starwars";
          };

          update = {
            type = "app";
            program = "${self.packages.${system}.update}/bin/starwars-update";
          };
        };
      }
    );
}
