using System;
using Microsoft.EntityFrameworkCore.Migrations;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace GuitarCogData.Migrations
{
    /// <inheritdoc />
    public partial class tabandfilefixes : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Images");

            //самописный
            migrationBuilder.DropColumn("AvatarImageId", "AspNetUsers");
            migrationBuilder.AddColumn<Guid>(
                name: "AvatarImageId",
                table: "AspNetUsers",
                type: "uuid",
                nullable: true
            );
            
            //не работает - 42804: столбец "AvatarImageId" нельзя автоматически привести к типу uuid
            /*migrationBuilder.AlterColumn<Guid>(
                name: "AvatarImageId",
                table: "AspNetUsers",
                type: "uuid",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);*/

            migrationBuilder.CreateTable(
                name: "Files",
                columns: table => new
                {
                    Id = table.Column<Guid>(type: "uuid", nullable: false),
                    FileName = table.Column<string>(type: "text", nullable: false),
                    Bytes = table.Column<byte[]>(type: "bytea", nullable: false),
                    ContentType = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Files", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Tabs",
                columns: table => new
                {
                    Id = table.Column<long>(type: "bigint", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    TabFileId = table.Column<Guid>(type: "uuid", nullable: false),
                    Name = table.Column<string>(type: "text", nullable: false),
                    AuthorId = table.Column<string>(type: "text", nullable: true),
                    LoadDateTime = table.Column<DateTimeOffset>(type: "timestamp with time zone", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Tabs", x => x.Id);
                    table.ForeignKey(
                        name: "FK_Tabs_AspNetUsers_AuthorId",
                        column: x => x.AuthorId,
                        principalTable: "AspNetUsers",
                        principalColumn: "Id");
                    table.ForeignKey(
                        name: "FK_Tabs_Files_TabFileId",
                        column: x => x.TabFileId,
                        principalTable: "Files",
                        principalColumn: "Id",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_AspNetUsers_AvatarImageId",
                table: "AspNetUsers",
                column: "AvatarImageId");

            migrationBuilder.CreateIndex(
                name: "IX_Tabs_AuthorId",
                table: "Tabs",
                column: "AuthorId");

            migrationBuilder.CreateIndex(
                name: "IX_Tabs_TabFileId",
                table: "Tabs",
                column: "TabFileId");

            migrationBuilder.AddForeignKey(
                name: "FK_AspNetUsers_Files_AvatarImageId",
                table: "AspNetUsers",
                column: "AvatarImageId",
                principalTable: "Files",
                principalColumn: "Id");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_AspNetUsers_Files_AvatarImageId",
                table: "AspNetUsers");

            migrationBuilder.DropTable(
                name: "Tabs");

            migrationBuilder.DropTable(
                name: "Files");

            migrationBuilder.DropIndex(
                name: "IX_AspNetUsers_AvatarImageId",
                table: "AspNetUsers");

            //самописный
            migrationBuilder.DropColumn("AvatarImageId", "AspNetUsers");
            migrationBuilder.AddColumn<Guid>(
                name: "AvatarImageId",
                table: "AspNetUsers",
                type: "text",
                nullable: true
            );
            
            //не работает - 42804: столбец "AvatarImageId" нельзя автоматически привести к типу uuid
            /*migrationBuilder.AlterColumn<string>(
                name: "AvatarImageId",
                table: "AspNetUsers",
                type: "text",
                nullable: true,
                oldClrType: typeof(Guid),
                oldType: "uuid",
                oldNullable: true);*/

            migrationBuilder.CreateTable(
                name: "Images",
                columns: table => new
                {
                    Id = table.Column<string>(type: "text", nullable: false),
                    Bytes = table.Column<byte[]>(type: "bytea", nullable: false),
                    ContentType = table.Column<string>(type: "text", nullable: false),
                    FileName = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Images", x => x.Id);
                });
        }
    }
}
