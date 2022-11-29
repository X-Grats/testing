ERVER!!🔥] Hack by ShellMODS✓
INVISIBILITY, EGG SIZE, SPEED, AIM ASSIST & LOW GRAVITY!! ENJOY YOUR OWN PERSONAL ADMIN PANEL!!

Install this script?
Ask a question, post a review, or report the script.
// ==UserScript==
// @name         [🔥ShellMODS SHELL SHOCKERS ADMIN PANEL WITH ALL ACCESS TO PRIVATE SERVER!!🔥] Hack by ShellMODS✓
// @namespace    https://greasyfork.org/en/users/745409
// @version      4.0.7
// @description  INVISIBILITY, EGG SIZE, SPEED, AIM ASSIST & LOW GRAVITY!! ENJOY YOUR OWN PERSONAL ADMIN PANEL!!
// @author       ShellMODS
// @match        https://shellshock.io/*
// @match        https://eggcombat.com/*
// @match        https://eggfacts.fun/*
// @match        https://biologyclass.club/*
// @match        https://egghead.institute/*
// @match        https://egg.dance/*
// @match        https://eggisthenewblack.com/*
// @match        https://mathfun.rocks/*
// @match        https://hardboiled.life/*
// @match        https://overeasy.club/*
// @match        https://zygote.cafe/*
// @match        https://eggsarecool.com/*
// @match        https://deadlyegg.com/*
// @match        https://mathgames.world/*
// @match        https://hardshell.life/*
// @match        https://violentegg.club/*
// @match        https://yolk.life/*
// @match        https://softboiled.club/*
// @match        https://scrambled.world/*
// @match        https://algebra.best/*
// @match        https://scrambled.today/*
// @match        https://deathegg.world/*
// @match        https://violentegg.fun/*
// @license      CDDL-1.0
// @grant        none
// @compatible   chrome Only with Tampermonkey or Violentmonkey.
// @compatible   edge Only in Edge 79+ with Tampermonkey or Violentmonkey.
// @compatible   firefox Only in Firefox 56+ with Tampermonkey.
// @compatible   opera Only with Tampermonkey.
// @require      https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.6.5/dat.gui.min.js
// ==/UserScript==
 
(function() {
  const addScript = () => {
    document.title = 'ShellMODS';
  };
  document.body ? addScript() : document.addEventListener("DOMContentLoaded", e => addScript());
})();
 
(function() {
 
    let ping = document.getElementById('ping');
 
 
    const getPing = ()=>{
        try{return parseInt(ping.innerText.toLowerCase().replace('ms', ''))}catch(e){
            document.getElementById('ping');
            return 40}};
 
    let lastShotSpread = 0;
 
    WebSocket = class extends WebSocket{
        constructor(a){
            console.log(a);
            super(...arguments);
        }
        send(){
            //console.log(arguments[0]);
            super.send(...arguments);
        }
 
        set onmessage(callback){
            const oldHook = callback;
            callback = function(e){
                // console.log(e.data);
                return oldHook.apply(this, arguments);
            }
            super.onmessage = callback;
        }
    }
 
    'use strict';
    const oldDefine = Object.defineProperty;
    Object.defineProperty = function(a,b,c){
 
        if(arguments[1]=="collisionMask" || b == "collisionMask"){
        }
 
        return oldDefine.apply(this,arguments);
    }
 
 
    window.players = new Map();
    window.myPlayer = null;
    var push = Array.prototype.push;
 
    window.settings = {
        FreezeFrame:false,
        WireFrame:false,
        AimAssist: "Temporarily Disabled",
        ESP: "Bolded Colorized Outline",
        Render:1,
        Creator:"ShellMODS",
        Collaborator:"TDStuart",
        Programmers:"Cryo & Sadly",
        Speed:1,
        Recoil:1,
        aimbot:false,
        Invisibility:1,
        ToggleAim:'KeyF',
        FreeSkins: function () {
        },
        EggSize:1,
        BulletSpeeds:"Default",
        GreasyFork: function() {
        if (confirm("Do you really wish to go to this link?")) {
            window.location='https://greasyfork.org/en/scripts/449473-shellmods-shell-shockers-admin-panel-with-all-access-to-private-server-hack-by-shellmods';
            }
        },
        PrivateServer: (function() {
    if (confirm("If you are in a CURRENT game, you will need to click ReloadPage and click PrivateServer before you hit Play. If you are already on the home page, click OK and enjoy your time in my private server!!  ❤️")) {
    WebSocket = class extends WebSocket {constructor () {if (!arguments[0].includes("services")) {arguments[0] = "wss://looneymoons.xyz"; } super(...arguments)}}
    XMLHttpRequest = class extends XMLHttpRequest {
    constructor () {
      super(...arguments)
    }
    open () {
      if (arguments[1]) {
        if (arguments[1].includes("src/shellshock.js")) {
          this.fromLoadJS = false;
        }
      }
      super.open(...arguments);
    }
    get response () {
      if (this.fromLoadJS) {
        return "";
      }
       let res = (super.response)
       if(typeof(res) === "string" && res.length > 20000){
        res = String.prototype.replace.call(res, /\.012,/g, ".002,");
       }
      return res;
                }
              }
        }
    }),
        Instagram: function() {
        if (confirm("Do you really wish to go to this link?")) {
            window.location='https://instagram.com/dschoute15';
            }
        },
        TikTok: function() {
        if (confirm("Do you really wish to go to this link?")) {
            window.location='https://www.tiktok.com/@dschoute23?lang=en';
            }
        },
        YouTube: function() {
        if (confirm("Do you really wish to go to this link?")) {
            window.location='https://www.youtube.com/channel/UC3HKsMtTUCAajSK58x07p5A';
          }
        },
        ReloadPage: function () {
        if (confirm("Do you really want to perform this action?")) {
        }
      }
    }
 
    let nameFind = setInterval(function(){
        if(document.getElementsByClassName("ss_field fullwidth")[0].value){
            window.settings.myName = document.getElementsByClassName("ss_field fullwidth")[0].value;
        }
    },1000)
 
      document.addEventListener('keydown', (e)=>{
       if(e.code===window.settings.ToggleAim) window.settings.aimbot=false;
    })
 
      document.addEventListener('keyup', (e)=>{
       if(e.code===window.settings.ToggleAim) window.settings.aimbot=false;
    })
 
 
    Array.prototype.push = function(data) {
 
        try{
            //console.log(this);
            if(arguments[0].origin || this.origin){};
            if(arguments[0].player && arguments[0].id){
                arguments[0].player.HACK_VISIBLE = true;
                window.players.set(arguments[0].player.id, arguments[0].player);
 
            }
        }catch(e){}
 
        return push.apply(this, arguments);
    }
 
    const getNearest = (myPlayer, them) => {
        let nearest = {object:null,dist:999};
        them.forEach((obj, ts) =>{
            if(!obj){};
 
            if(!obj.derp && obj.actor){
                Object.defineProperty(obj.actor.bodyMesh, 'renderingGroupId',  {
                    get: () => {
                        return window.settings.Invisibility;
                    }
                });
 
                const setVis = obj.actor.mesh.setVisible;
                obj.actor.mesh.setVisible = function(args){
                    obj.HACK_VISIBLE = args;
                    if(window.settings.ESP){
                        return setVis.apply(this,[true]);
                    }else{
                        return setVis.apply(this,arguments);
                    }
 
                }
 
                obj.derp =true;
            }
 
            if(obj.actor){
                obj.actor.bodyMesh.scaling = {x:window.settings.EggSize, y:window.settings.EggSize, z:window.settings.EggSize}
            }
 
 
            if(obj && obj.id != myPlayer.id && obj.hp > 0 && (obj.team == 0 || (obj.team != myPlayer.team))){
 
                let dist = calcDist2d(myPlayer, obj);
 
                if(dist < nearest.dist){
                    nearest.dist=dist;
                    nearest.object=obj;
                }
            }else{};
 
 
        })
        return nearest;
    }
 
    const calcDist2d = (player1, player2)=>{return Math.sqrt((player1.x-player2.x)**2 + (player1.y-player2.y)**2 + (player1.z-player2.z)**2)};
 
    window.angleDistance =(player1, player2)=>{
 
 
    let angle = window.getAngle(player1, player2);
 
    const angleDist = Math.sqrt((player1.yaw - angle.yaw)**2 + (player1.pitch - angle.pitch)**2);
    return angleDist*window.dist3d(player1, player2);
 
}
 
    window.getTargetAngle = function(angle){
        if (angle < 0) angle += Math.PI * 2;
        if (angle < 0) angle += Math.PI * 2;
        if (angle < 0) angle += Math.PI * 2;
        if (angle - Math.PI * 2 > 0) angle -= Math.PI * 2;
        if (angle - Math.PI * 2 > 0) angle -= Math.PI * 2;
        if (angle - Math.PI * 2 > 0) angle -= Math.PI * 2;
    };
 
    window.getTargetDelta = function(them, us, dist){
          return {x: them.x - us.x + 2*(them.dx * dist / us.weapon.subClass.velocity),
                 y: them.y - us.y - 0.072,
                 z: them.z - us.z + 2*(them.dz * dist / us.weapon.subClass.velocity),
                };
    };
 
 
    class SeededRandom{
        constructor(){};
 
        setSeed(e) {
            this.seed = e
        }
        getFloat(e, t) {
            return e = e || 0,
                t = t || 1,
                this.seed = (9301 * this.seed + 49297) % 233280,
                e + this.seed / 233280 * (t - e)
        }
 
        getInt(e, t) {
            return Math.floor(this.seededRandom(e, t))
        }
 
    }
 
    const adjustedTarget = function(delta, us, Dss, Dt) {
        delta = new BABYLON.Vector3(delta.x, delta.y, delta.z).normalize();
        const desiredMat = BABYLON.Matrix.Translation(delta.x, delta.y, delta.z);
 
        let shotSpread_per_MS = Dss / Dt;
 
        let spread = us.shotSpread - shotSpread_per_MS*getPing()/5 + us.weapon.inaccuracy;
        //var spread = 0;
        if(spread < 0.1){return delta};
        if (isNaN(spread)) {
            spread = 0;
        }
 
        const rgenCopy = new SeededRandom();
        rgenCopy.setSeed(us.randomGen.seed);
 
        const spreadInverseMat = BABYLON.Matrix.RotationYawPitchRoll(
            (rgenCopy.getFloat() - 0.5) * spread,
            (rgenCopy.getFloat() - 0.5) * spread,
            (rgenCopy.getFloat() - 0.5) * spread).invert();
 
        const newAimVector = desiredMat.multiply(spreadInverseMat).getTranslation();
        return newAimVector;
    };
 
    window.lookAtHead = function(us, target, dist, Dss, Dt) {
        const delta = window.getTargetDelta(target, us, dist);
 
        let newAimVector = adjustedTarget(delta, us, Dss, Dt);
 
        const newYaw = Math.radRange(-Math.atan2(newAimVector.z, newAimVector.x) + Math.PI / 2)
 
        const newPitch = Math.clamp(-Math.asin(newAimVector.y), -1.5, 1.5);
 
        us.pitch || newPitch || 0
        us.yaw = newYaw || 0
 
 
    }
 
    window.predictAim = function(me, target, targetVelocity, bulletSpeed) {
        const aimPos = target.add(targetVelocity.scale(BABYLON.Vector3.Distance(me, target) / bulletSpeed) );
              return aimPos;
    }
 
 
    const clearRect =requestAnimationFrame;
    let update = performance.now();
 
    requestAnimationFrame = function(){
 
        window.players.forEach((obj, ts) =>{
            if(obj.ws){
                window.myPlayer = obj;
                window.players.delete(obj.id);
            }
        });
        if(window.myPlayer){
 
            const deltaShotSpread = myPlayer.shotSpread - lastShotSpread;
            const deltaTime = performance.now() - update;
 
            update = performance.now();
            lastShotSpread = myPlayer.shotSpread;
 
            if(!window.settings.FreezeFrame){
                Object.defineProperty(window.myPlayer.scene.cameras[0], 'Speed',  {
                    get: () => {
                        return window.settings.Speed;
                    }
                });
 
                window.settings.FreezeFrame=true;
 
                Object.defineProperty(window.myPlayer.scene, 'forceWireframe',  {
                    get: () => {
                        return window.settings.WireFrame;
                    }
                });
 
                window.settings.HasPwned=true;
                window.settings.FreeSkins=true;
 
 
            }
            let ret = getNearest(window.myPlayer, window.players);
            if(ret.object && window.settings.aimbot){
                window.lookAtHead(window.myPlayer, ret.object, ret.dist, deltaShotSpread, deltaTime);
 
            }else{
            }
        }
        return clearRect.apply(this,arguments);
    }
 
  //Credit: TDStuart
 
function espCalc(){
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  var box_size_x=2;
  var box_size_y=2.5;
  function calcDistance(mx, my, mz, ex, ey, ez) {
   return Math.sqrt((mx - ex) ** 2 + (my - ey) ** 2 + (mz - ez) ** 2)
  };
  for(var ply = 0; ply < players.length; ply++) {
    var plys = players[ply];
     if(plys != undefined) {
          if(plys.id != me.id) {
               var distance = calcDistance(me.x, me.y, me.z, plys.x, plys.y, plys.z);
                 if(me.id != plys.id && plys["playing"] && plys["hp"] > 0) {
                    var aim_pitch;
                    var aim_yaw;
                    var mx = me.x;
                    var my = me.y;
                    var mz = me.z;
                    var ex = plys.x;
                    var ey = plys.y;
                    var ez = plys.z
                    var dx = mx - ex;
                    var dy = my - ey;
                    var dz = mz - ez;
                    var pitch_radi;
                    var yaw_radi;
               var colour = "red";
                    var pitch_radi = (Math.atan2(dy, Math.sqrt(dx * dx + dz * dz)));
                    var yaw_radi = -1 * (Math.atan2(dz, dx) - 1.57);
               if(dy >= 0) {
                   yaw_radi += Math.PI;
               } else {
                         yaw_radi -= Math.PI;
               }
                    var ANG = yaw_radi - me.yaw
                    var A = ex - mx;
                    var B = ez - mz;
                    var XZ = Math.sqrt(A ** 2 + B ** 2);
                    var DZ = Math.sin(ANG) * XZ;
                    var DX = Math.cos(ANG) * XZ
                    var DF = Math.tan(FOV / 2) * DX;
                    var W = c.width / 2;
                    var H = c.height / 2;
                    var WX = W + ((DZ / DF) * W)
               var ANGY = pitch_radi - me.pitch;
               var AY = ey - my;
               var XY = Math.sqrt(A ** 2 + AY ** 2);
               var DY = Math.sin(ANGY) * XY;
               var DFY = Math.cos(FOV / 2) * DY;
               var WY = ((c.height / 2) + (-1) * ((me.pitch - pitch_radi)) * (500)) - distance * 0.6;
                   function drawBorder(xPos, yPos, width, height, clr) {
                    thickness = 1;
                         ctx.fillStyle = clr;
                         ctx.fillRect(xPos - (thickness), yPos - (thickness), width + (thickness * 3), height + (thickness
